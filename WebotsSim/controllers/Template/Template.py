# Changes Working Directory to be at the root of FAIRIS-Lite
import os
os.chdir("../..")

# Import MyRobot Class
from WebotsSim.libraries.MyRobot import MyRobot

# Create the robot instance.
robot = MyRobot()

# Loads the environment from the maze file
maze_file = 'worlds/mazes/Labs/Lab3/Lab3_Task2_2.xml'
robot.load_environment(maze_file)

# Move robot to a random staring position listed in maze file
robot.move_to_start()

# Main Control Loop for Robot
while robot.experiment_supervisor.step(robot.timestep) != -1:

    print("Max rotational motor velocity: ", robot.max_motor_velocity)

    # Reads and Prints Distance Sensor Values
    print("Front Left Distance Sensor: ", robot.get_front_left_distance_reading())
    print("Front Right Distance Sensor: ", robot.get_front_right_distance_reading())
    print("Rear Left Distance Sensor: ", robot.get_rear_left_distance_reading())
    print("Rear Right Distance Sensor: ", robot.get_rear_right_distance_reading())

    # Reads and Prints Robot's Encoder Readings
    print("Motor Encoder Readings: ", robot.get_encoder_readings())

    # Reads and Prints Robot's Lidar Readings Relative to Robot's Position
    print("Lidar Front Reading", robot.get_lidar_range_image()[400])
    print("Lidar Right Reading", robot.get_lidar_range_image()[600])
    print("Lidar Rear Reading", robot.get_lidar_range_image()[0])
    print("Lidar Left Reading", robot.get_lidar_range_image()[200])

    # Sets the robot's motor velocity to 20 rad/sec
    robot.set_right_motors_velocity(20)
    robot.set_left_motors_velocity(20)

    # Calculates distance the wheel has turned since beginning of simulation
    distance_front_left_wheel_traveled = robot.wheel_radius * robot.get_front_left_motor_encoder_reading()

    # Stops the robot after the robot moves a distance of 1.5 meters
    if distance_front_left_wheel_traveled > 1.5:
        robot.stop()
        break





