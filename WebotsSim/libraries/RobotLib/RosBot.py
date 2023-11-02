import math

import matplotlib.pyplot as plt

from WebotsSim.libraries.RobotLib.Environment import *
from controller import Supervisor


# Custom Class of RosBot offered by Webots
#   Webots: https://www.cyberbotics.com/doc/guide/rosbot
#   Sepecs: https://husarion.com/manuals/rosbot/#specification
class RosBot(Supervisor):

    # Initiilize an instance of Webots Harrison's RosBot
    def __init__(self):

        # Inherent from Webots Robot Class: https://cyberbotics.com/doc/reference/robot
        self.experiment_supervisor = Supervisor()

        # Add a display to plot the place cells as they are generated
        self.display = self.experiment_supervisor.getDevice('User Display')
        self.display.setOpacity(1.0)

        # Sets Supervisor Root Nodes
        self.root_node = self.experiment_supervisor.getRoot()
        self.children_field = self.root_node.getField('children')
        self.robot_node = self.experiment_supervisor.getFromDef('Agent')
        self.robot_translation_field = self.robot_node.getField('translation')
        self.robot_rotation_field = self.robot_node.getField('rotation')

        # Physical Robot Specifications
        self.wheel_radius = .043  # meters
        self.axel_length = .265  # meters
        self.axel_distance = .053  # meters

        # Define all systems and makes them class attributes
        self.timestep = int(self.experiment_supervisor.getBasicTimeStep())

        # Webots Rotational Motors: https://cyberbotics.com/doc/reference/motor
        self.front_left_motor = self.experiment_supervisor.getDevice('front left wheel motor')
        self.front_right_motor = self.experiment_supervisor.getDevice('front right wheel motor')
        self.rear_left_motor = self.experiment_supervisor.getDevice('rear left wheel motor')
        self.rear_right_motor = self.experiment_supervisor.getDevice('rear right wheel motor')
        self.all_motors = [self.front_left_motor,
                           self.front_right_motor,
                           self.rear_left_motor,
                           self.rear_right_motor]
        self.max_motor_velocity = self.rear_left_motor.getMaxVelocity()

        # Initialize robot's motors
        for motor in self.all_motors:
            motor.setPosition(float('inf'))
            motor.setVelocity(0.0)

        # Webots Wheel Positional Sensors: https://www.cyberbotics.com/doc/reference/positionsensor
        self.front_left_encoder = self.experiment_supervisor.getDevice('front left wheel motor sensor')
        self.front_right_encoder = self.experiment_supervisor.getDevice('front right wheel motor sensor')
        self.rear_left_encoder = self.experiment_supervisor.getDevice('rear left wheel motor sensor')
        self.rear_right_encoder = self.experiment_supervisor.getDevice('rear right wheel motor sensor')
        self.all_encoders = [self.front_left_encoder,
                             self.front_right_encoder,
                             self.rear_left_encoder,
                             self.rear_right_encoder]

        # Initialize robot's encoders
        for encoder in self.all_encoders:
            encoder.enable(self.timestep)

        # Webots Astra Camera: https://cyberbotics.com/doc/guide/range-finder-sensors#orbbec-astra
        self.depth_camera = self.experiment_supervisor.getDevice('camera depth')
        self.depth_camera.enable(self.timestep)

        # Webots Camera: https://cyberbotics.com/doc/reference/camera
        self.rgb_camera = self.experiment_supervisor.getDevice('camera rgb')
        self.rgb_camera.enable(self.timestep)
        self.rgb_camera.recognitionEnable(self.timestep)

        # Webots RpLidarA2: https://www.cyberbotics.com/doc/guide/lidar-sensors#slamtec-rplidar-a2
        self.lidar = self.experiment_supervisor.getDevice('lidar')
        self.lidar.enable(self.timestep)
        self.lidar.enablePointCloud()

        # Webots IMU: https://www.cyberbotics.com/doc/guide/imu-sensors#mpu-9250
        # Webots IMU Accelerometer: https://www.cyberbotics.com/doc/reference/accelerometer
        self.accelerometer = self.experiment_supervisor.getDevice('imu accelerometer')
        self.accelerometer.enable(self.timestep)
        # Webots IMU Gyro: https://www.cyberbotics.com/doc/reference/gyro
        self.gyro = self.experiment_supervisor.getDevice('imu gyro')
        self.gyro.enable(self.timestep)
        # Webots IMU Compass: https://www.cyberbotics.com/doc/reference/compass
        self.compass = self.experiment_supervisor.getDevice('imu compass')
        self.compass.enable(self.timestep)

        # Webots GPS:
        self.gps = self.experiment_supervisor.getDevice('gps')
        self.gps.enable(self.timestep)

        # Webots Distance Sensors: https://www.cyberbotics.com/doc/reference/distancesensor
        self.front_left_ds = self.experiment_supervisor.getDevice('front left distance sensor')
        self.front_right_ds = self.experiment_supervisor.getDevice('front right distance sensor')
        self.rear_left_ds = self.experiment_supervisor.getDevice('rear left distance sensor')
        self.rear_right_ds = self.experiment_supervisor.getDevice('rear right distance sensor')

        self.all_distance_sensors = [self.front_left_ds,
                                     self.front_right_ds,
                                     self.rear_right_ds,
                                     self.rear_left_ds]

        for ds in self.all_distance_sensors:
            ds.enable(self.timestep)

        self.sensor_calibration()

    # Preforms one timestep to update all sensors should be used when initializing robot and after teleport
    def sensor_calibration(self):
        while self.experiment_supervisor.step(self.timestep) != -1:
            break

    # Reads the robot's IMU compass and return bearing in degrees
    #   North   -> 90
    #   East    -> 0 or 360
    #   South   -> 270
    #   West    -> 180
    def get_compass_reading(self):
        compass_reading = self.compass.getValues()
        rad = math.atan2(compass_reading[0], compass_reading[1]) + math.pi / 2
        bearing = (rad - math.pi / 2) / math.pi * 180.0
        if bearing < 0.0:
            bearing += 360.0
        return round(bearing)

    # Reads current encoder readings and return an array of encoder positions:
    #   [front_left, front_right, rear_right, rear_right]
    def get_encoder_readings(self):
        return [readings.getValue() for readings in self.all_encoders]

    # Caps the motor velocities to ensure PID calculations do no exceed motor speeds
    def velocity_saturation(self, motor_velocity, suppress=False):
        if motor_velocity > self.max_motor_velocity:
            if not suppress:
                print("Provided Motor Velocity is to large set to: ", self.max_motor_velocity)
            return self.max_motor_velocity
        elif motor_velocity < -1 * self.max_motor_velocity:
            if not suppress:
                print("Provided Motor Velocity is to large set to: ", -1 * self.max_motor_velocity)
            return -1 * self.max_motor_velocity
        else:
            return motor_velocity

    # Sets Front Left Motor Velocity (rad/sec)
    def set_front_left_motor_velocity(self, velocity, suppress=False):
        self.front_left_motor.setVelocity(self.velocity_saturation(velocity, suppress=suppress))

    # Sets Front Right Motor Velocity (rad/sec)
    def set_front_right_motor_velocity(self, velocity, suppress=False):
        self.front_right_motor.setVelocity(self.velocity_saturation(velocity, suppress=suppress))

    # Sets Rear Left Motor Velocity (rad/sec)
    def set_rear_left_motor_velocity(self, velocity, suppress=False):
        self.rear_left_motor.setVelocity(self.velocity_saturation(velocity, suppress=suppress))

    # Sets Rear Right Motor Velocity (rad/sec)
    def set_rear_right_motor_velocity(self, velocity, suppress=False):
        self.rear_right_motor.setVelocity(self.velocity_saturation(velocity, suppress=suppress))

    # Sets Right Motors Velocity (rad/sec)
    def set_right_motors_velocity(self, velocity, suppress=False):
        self.front_right_motor.setVelocity(self.velocity_saturation(velocity, suppress=suppress))
        self.rear_right_motor.setVelocity(self.velocity_saturation(velocity, suppress=suppress))

    # Sets Left Motors Velocity (rad/sec)
    def set_left_motors_velocity(self, velocity, suppress=False):
        self.front_left_motor.setVelocity(self.velocity_saturation(velocity, suppress=suppress))
        self.rear_left_motor.setVelocity(self.velocity_saturation(velocity, suppress=suppress))

    # Sets all motors speed to 0
    def stop(self):
        for motor in self.all_motors:
            motor.setVelocity(0)

    # Sets all motors speed to velocity
    def go_forward(self, velocity=1):
        for motor in self.all_motors:
            motor.setVelocity(self.velocity_saturation(velocity))

    # Gets Current Front Left Motor Encoder Reading (meters)
    def get_front_left_motor_encoder_reading(self):
        return self.front_left_encoder.getValue()

    # Gets Current Front Right Motor Encoder Reading (meters)
    def get_front_right_motor_encoder_reading(self):
        return self.front_right_encoder.getValue()

    # Gets Current Rear Left Motor Encoder Reading (meters)
    def get_rear_left_motor_encoder_reading(self):
        return self.rear_left_encoder.getValue()

    # Gets Current Rear Right Motor Encoder Reading (meters)
    def get_rear_right_motor_encoder_reading(self):
        return self.rear_right_encoder.getValue()

    # Gets Current Front Left Distance Sensor Reading (meters)
    def get_front_left_distance_reading(self):
        return self.front_left_ds.getValue()

    # Gets Current Front Right Distance Sensor Reading (meters)
    def get_front_right_distance_reading(self):
        return self.front_right_ds.getValue()

    # Gets Current Rear Left Distance Sensor Reading (meters)
    def get_rear_left_distance_reading(self):
        return self.rear_left_ds.getValue()

    # Gets Current Rear Right Distance Sensor Reading (meters)
    def get_rear_right_distance_reading(self):
        return self.rear_right_ds.getValue()

    # Get Lidar Range Image (meters)
    def get_lidar_range_image(self):
        return self.lidar.getRangeImage()

    # Supervisor Functions: allows robot to control the simulation
    # DO NOT MODIFY: unless you are attempting to manipulate the webots world simulations!!!

    # Takes in a xml maze file and creates the walls, starting locations, and goal locations
    def load_environment(self, maze_file):
        self.maze = Maze(maze_file)
        self.obstical_nodes = []
        self.boundry_wall_nodes = []
        self.landmark_nodes = []
        for obstacles in self.maze.obstacles:
            self.children_field.importMFNodeFromString(-1, obstacles.get_webots_node_string())
            self.obstical_nodes.append(self.experiment_supervisor.getFromDef('Obstacle'))
        for boundary_wall in self.maze.boundary_walls:
            self.children_field.importMFNodeFromString(-1, boundary_wall.get_webots_node_string())
            self.boundry_wall_nodes.append(self.experiment_supervisor.getFromDef('Obstacle'))
        for landmark in self.maze.landmarks:
            self.children_field.importMFNodeFromString(-1,landmark.get_webots_node_string())
            self.landmark_nodes.append(self.experiment_supervisor.getFromDef('Landmark'))

    # Teleports the robot to the point (x,y,z)
    def teleport_robot(self, x=0.0, y=0.0, z=0.0, theta=math.pi/3):
        self.robot_translation_field.setSFVec3f([x, y, z])
        self.robot_rotation_field.setSFRotation([0,0,1,theta])
        self.sensor_calibration()

    # Moves the robot to a random starting position
    def move_to_start(self):
        starting_position = self.maze.get_random_starting_position()
        self.starting_position = starting_position
        self.teleport_robot(starting_position.x, starting_position.y,theta=starting_position.theta)

    # Plots Place cells and shows them on the Display
    def update_display(self, fig):
        fig.savefig('DisplayCache/temp.png')
        plt.close(fig)
        while self.experiment_supervisor.step(self.timestep) != -1:
            ir = self.display.imageLoad('DisplayCache/temp.png')
            self.display.imagePaste(ir, 0, 0, True)
            break
