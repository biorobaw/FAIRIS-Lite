import math
import matplotlib.pyplot as plt

from controller import Supervisor
from fairis_lib.mapping_utils.environment import Maze

class HamBot(Supervisor):

    # Initiilize an instance of Webots Harrison's RosBot
    def __init__(self):

        # Inherent from Webots Robot Class: https://cyberbotics.com/doc/reference/robot
        self.experiment_supervisor = Supervisor()

        # Sets Supervisor Root Nodes
        self.root_node = self.experiment_supervisor.getRoot()
        self.children_field = self.root_node.getField('children')
        self.robot_node = self.experiment_supervisor.getSelf()
        self.robot_translation_field = self.robot_node.getField('translation')
        self.robot_rotation_field = self.robot_node.getField('rotation')

        # Physical Robot Specifications
        self.wheel_radius = .045  # meters
        self.axel_length = .184  # meters

        # Define all systems and makes them class attributes
        self.timestep = int(self.experiment_supervisor.getBasicTimeStep())

        # Webots Rotational Motors: https://cyberbotics.com/doc/reference/motor
        self.left_motor = self.experiment_supervisor.getDevice('left motor')
        self.right_motor = self.experiment_supervisor.getDevice('right motor')
        self.all_motors = [self.left_motor, self.right_motor]
        self.max_motor_velocity = self.left_motor.getMaxVelocity()

        # Initialize robot's motors
        for motor in self.all_motors:
            motor.setPosition(float('inf'))
            motor.setVelocity(0.0)

        # Webots Wheel Positional Sensors: https://www.cyberbotics.com/doc/reference/positionsensor
        self.left_encoder = self.experiment_supervisor.getDevice('left wheel encoder')
        self.right_encoder = self.experiment_supervisor.getDevice('right wheel encoder')
        self.all_encoders = [self.left_encoder, self.right_encoder]

        # Initialize robot's encoders
        for encoder in self.all_encoders:
            encoder.enable(self.timestep)


        # Webots Camera: https://cyberbotics.com/doc/reference/camera
        self.camera = self.experiment_supervisor.getDevice('camera')
        self.camera.enable(self.timestep)
        self.camera.recognitionEnable(self.timestep)

        # Webots RpLidarA2: https://www.cyberbotics.com/doc/guide/lidar-sensors#slamtec-rplidar-a2
        self.lidar = self.experiment_supervisor.getDevice('lidar')
        self.lidar.enable(self.timestep)
        self.lidar.enablePointCloud()

        # Webots IMU: https://www.cyberbotics.com/doc/guide/imu-sensors#mpu-9250
        # Webots IMU Accelerometer: https://www.cyberbotics.com/doc/reference/accelerometer
        self.imu = self.experiment_supervisor.getDevice('imu')
        self.imu.enable(self.timestep)

        # Webots GPS:
        self.gps = self.experiment_supervisor.getDevice('gps')
        self.gps.enable(self.timestep)

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
    # TODO: fix to work with new imu functions
    def get_compass_reading(self):
        compass_reading = self.imu.getRollPitchYaw()
        bearing = math.degrees(compass_reading[-1])
        if bearing < 0.0:
            bearing += 360.0
        return round(bearing)

    # Reads current encoder readings and return an array of encoder positions:
    #   [left, right]
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
    def set_left_motor_velocity(self, velocity, suppress=False):
        self.left_motor.setVelocity(self.velocity_saturation(velocity, suppress=suppress))

    # Sets Front Right Motor Velocity (rad/sec)
    def set_right_motor_velocity(self, velocity, suppress=False):
        self.right_motor.setVelocity(self.velocity_saturation(velocity, suppress=suppress))

    # Sets all motors speed to 0
    def stop(self):
        for motor in self.all_motors:
            motor.setVelocity(0)

    # Sets all motors speed to velocity
    def go_forward(self, velocity=1):
        for motor in self.all_motors:
            motor.setVelocity(self.velocity_saturation(velocity))

    # Gets Current Front Left Motor Encoder Reading (meters)
    def get_left_motor_encoder_reading(self):
        return self.left_encoder.getValue()

    # Gets Current Front Right Motor Encoder Reading (meters)
    def get_right_motor_encoder_reading(self):
        return self.right_encoder.getValue()

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


