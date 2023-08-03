import os
os.chdir("../..")

"""ExperimentSupervisor controller."""
from WebotsSim.libraries.RosBot import RosBot

# create the robot/supervisor instance.
robot = RosBot()

# Loads the environment from the maze file
maze_file = 'worlds/mazes/samples/WM20.xml'
robot.load_environment(maze_file)

# Move robot/supervisor to a random staring position listed in maze file
robot.move_to_random_start()

# Robot preforms each of the 8 allocentric actions
for i in range(8):
    robot.preform_action(i)
    robot_x, robot_y, robot_theta = robot.get_robot_pose()

# After actions are preformed simulation is reset
robot.experiment_supervisor.simulationReset()


