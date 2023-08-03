import os
os.chdir("../..")

"""ExperimentSupervisor controller."""
from WebotsSim.libraries.RosBot import RosBot


maze_file = 'worlds/mazes/samples/WM20.xml'

# create the robot/supervisor instance.
robot = RosBot()

# Loads the environment from the maze file
robot.load_environment(maze_file)

# Show basic robot/supervisor functions
robot.move_to_random_start()

# Creates Place Cell Network

for i in range(8):
    robot.preform_action(i)
    robot_x, robot_y, robot_theta = robot.get_robot_pose()

robot.experiment_supervisor.simulationReset()


