# Changes Working Directory to be at the root of FAIRIS-Lite
import os
os.chdir("../..")

# Import MyRobot Class
from WebotsSim.libraries.MyRobot import MyRobot

# Create the robot instance.
robot = MyRobot()

# Loads the environment from the maze file

mazes = [
    "worlds/mazes/Labs/Lab2/Lab2_1.xml",
    "worlds/mazes/Labs/Lab2/Lab2_2.xml",
    "worlds/mazes/Labs/Lab2/Lab2_3.xml"
]

robot.load_environment(mazes[0])

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
    print("Direction: ", robot.get_compass_reading())

    # Reads and Prints Robot's Encoder Readings
    print("Motor Encoder Readings: ", robot.get_encoder_readings())

    # Calculates distance the wheel has turned since beginning of simulation
    distance_front_left_wheel_traveled = robot.wheel_radius * robot.get_front_left_motor_encoder_reading()
    distance_front_right_wheel_traveled = robot.wheel_radius * robot.get_front_right_motor_encoder_reading()

    break

#Lab 1 Directions
robot.move_straight(15)
robot.print_pose()

robot.move_along_curve(0.5, 3.4)
robot.print_pose()

robot.move_straight(12.5)
robot.print_pose()

robot.move_along_curve(0.5, 3.4)
robot.print_pose()

robot.move_straight(2.5)
robot.print_pose()

robot.rotate_in_place(-90)
robot.print_pose()

robot.move_straight(9)
robot.print_pose()

robot.move_along_curve(-0.6, 13.4)
robot.print_pose()

robot.move_straight(6)
robot.print_pose()

robot.move_along_curve(0.5, 6.75)
robot.print_pose()

robot.move_straight(9.5)
robot.print_pose()