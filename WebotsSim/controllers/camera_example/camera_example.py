# Changes Working Directory to be at the root of FAIRIS-Lite
import os
os.chdir("../..")

# Import MyRobot Class
from WebotsSim.libraries.MyRobot import MyRobot

# Create the robot instance.
robot = MyRobot()

# Loads the environment from the maze file
maze_files = ['worlds/mazes/Labs/Lab1/Lab1_Task1.xml',
              'worlds/mazes/Labs/Lab1/Lab1_EC.xml',
              'worlds/mazes/Labs/Lab2/Lab2_Task1.xml',
              'worlds/mazes/Labs/Lab2/Lab2_Task2_1.xml',
              'worlds/mazes/Labs/Lab2/Lab2_Task2_2.xml',
              'worlds/mazes/Labs/Lab2/Lab2_EC_1.xml',
              'worlds/mazes/Labs/Lab2/Lab2_EC_2.xml',
              'worlds/mazes/Labs/Lab3/Lab3_Task1.xml',
              'worlds/mazes/Labs/Lab3/Lab3_Task2_1.xml',
              'worlds/mazes/Labs/Lab3/Lab3_Task2_2.xml',
              'worlds/mazes/Labs/Lab4/Lab4_Task1_1.xml',
              'worlds/mazes/Labs/Lab4/Lab4_Task1_2.xml',
              'worlds/mazes/Labs/Lab4/Lab4_Task1_3.xml',
              'worlds/mazes/Labs/Lab4/Lab4_Task2_1.xml',
              'worlds/mazes/Labs/Lab4/Lab4_Task2_2.xml',
              ]

robot.load_environment(maze_files[-5])

# Move robot to a random staring position listed in maze file
robot.move_to_start()

# Main Control Loop for Robot
while robot.experiment_supervisor.step(robot.timestep) != -1:

    # Checks to see if the camera detects recognition object
    # (Doc: https://cyberbotics.com/doc/reference/camera?tab-language=python)
    rec_objects = robot.rgb_camera.getRecognitionObjects()

    # if camera has detected an object
    if len(rec_objects) > 0:
        # extract detected an object
        landmark = rec_objects[0]
        # prints Info of detected object
        print('#######################################################################################################')
        print(f'Object ID: {landmark.getId()}')
        print(f'Object Location relative to the camera: \n X: {landmark.getPosition()[0]} \t Y: {landmark.getPosition()[1]} \t Z: {landmark.getPosition()[2]}')
        print(f'Object relative Size: \n Y: {landmark.getSize()[0]} \t Z: {landmark.getSize()[1]}')
        print(f'Object position on image: \n X: {landmark.getPositionOnImage()[0]} \t Y: {landmark.getPositionOnImage()[1]}')
        print(f'Object size on image: \n X: {landmark.getSizeOnImage()[0]} \t Y: {landmark.getSizeOnImage()[1]}')
        print(f'Object Color: R = {landmark.getColors()[0]} \t G = {landmark.getColors()[1]} \t B = {landmark.getColors()[2]}')


    # Sets the robot's motor velocity to 20 rad/sec
    robot.set_right_motors_velocity(-5)
    robot.set_left_motors_velocity(5)







