# Import MyRobot Class
from fairis_tools.my_robot import MyRobot
# Create the robot instance.
robot = MyRobot()

# Loads the environment from the maze file
maze_file = '../../worlds/PreviousCourses/Spring25/maze1.xml'
robot.load_environment(maze_file)

# Move robot to a random staring position listed in maze file
robot.move_to_start()

# Main Control Loop for Robot
while robot.experiment_supervisor.step(robot.timestep) != -1:

    print("Max rotational motor velocity: ", robot.max_motor_velocity)


    # Reads and Prints Robot's Encoder Readings
    print("Motor Encoder Readings: ", robot.get_encoder_readings())

    # Reads and Prints Robot's Lidar Readings Relative to Robot's Position
    print("Lidar Front Reading", robot.get_lidar_range_image()[180])
    print("Lidar Right Reading", robot.get_lidar_range_image()[90])
    print("Lidar Rear Reading", robot.get_lidar_range_image()[0])
    print("Lidar Left Reading", robot.get_lidar_range_image()[270])
    print("Simulation Time", robot.experiment_supervisor.getTime())

    # Sets the robot's motor velocity to 18 rad/sec
    robot.set_right_motor_velocity(18)
    robot.set_left_motor_velocity(18)

    # Calculates distance the wheel has turned since beginning of simulation
    distance_left_wheel_traveled = robot.wheel_radius * robot.get_left_motor_encoder_reading()
    robot.experiment_supervisor.getTime()

    # Stops the robot after the robot moves a distance of 1.5 meters
    if robot.experiment_supervisor.getTime() > 1.85:
        robot.stop()
        break





