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


# Variables
robot.load_environment(mazes[1])
wtf = "L"

# Move robot to a random staring position listed in maze file
robot.move_to_start()

while robot.experiment_supervisor.step(robot.timestep) != -1:
    print("Lidar Front Reading: ", robot.get_lidar_range_image()[400])
    print("Lidar Right Reading: ", robot.get_lidar_range_image()[600])
    print("Lidar Left Reading: ", robot.get_lidar_range_image()[200])
    print("Direction: ", robot.get_compass_reading())

    Vl, Vr = robot.wall_follow_PID(wall = wtf)
    robot.set_left_motors_velocity(Vl)
    robot.set_right_motors_velocity(Vr)

    fD = robot.get_lidar_range_image()[400]
    if fD < 0.45 and wtf == "R":
        robot.rotate_in_place(-90)
    if fD < 0.45 and wtf == "L":
        robot.rotate_in_place(90)