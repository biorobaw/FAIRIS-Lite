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

