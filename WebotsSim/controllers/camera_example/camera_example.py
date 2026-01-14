# Import MyRobot Class
from fairis_tools.my_robot import MyRobot

# Create the robot instance.
robot = MyRobot()

# Loads the environment from the maze file
maze_files = ['../../worlds/Spring26/maze0.xml',
              '../../worlds/Spring26/maze1.xml',
              '../../worlds/Spring26/maze2.xml',
              '../../worlds/Spring26/maze3.xml',
              '../../worlds/Spring26/maze4.xml',
              '../../worlds/Spring26/maze5.xml',
              '../../worlds/Spring26/maze6.xml',
              '../../worlds/Spring26/maze7.xml',
              '../../worlds/Spring26/maze8.xml'
              ]
robot.load_environment(maze_files[7])

# Move robot to a random staring position listed in maze file
robot.move_to_start()

start_pos = robot.starting_position
x = start_pos.x
y = start_pos.y
theta = start_pos.theta
print(x,y,theta)

# Main Control Loop for Robot
while robot.experiment_supervisor.step(robot.timestep) != -1:

    # Checks to see if the camera detects recognition object
    # (Doc: https://cyberbotics.com/doc/reference/camera?tab-language=python)
    rec_objects = robot.camera.getRecognitionObjects()

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
    robot.set_right_motor_velocity(-5)
    robot.set_left_motor_velocity(5)







