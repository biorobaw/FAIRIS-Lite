# RosBot Python Class

FAIRIS-Lite supports the use of the Husarion's ROSbot. The ROSbot robot is a ROS powered four-wheeled base, used for 
research and prototyping applications involving mapping, navigation, monitoring, reconnaissance and other behaviors. 
It is characterized by a set of features listed in Section [ROSbot Features](#rosbot-features). This model includes 
4x4 drive 
and 4 infra-red distance sensors (2 forward-facing, 2 rear-facing) for proximity measurements. It is also equipped 
with a LIDAR, an RGB-D camera and an IMU.

More information on specifications is available on [Webot's Documentation](https://webots.cloud/run?version=R2023b&url=https%3A%2F%2Fgithub.com%2Fcyberbotics%2Fwebots%2Fblob%2Freleased%2Fprojects%2Frobots%2Fhusarion%2Frosbot%2Fprotos%2FRosbot.proto)


## ROSbot Features

|Characteristics	| Values |
| --- | --- |
|Length |	200 mm |
|Width |	235 mm |
|Height	| 220 mm |
|Weight	| 2.84 kg |
|Max. forward/backward wheel speed	| 1 m/s |
|Max. forward/backward motor speed	| 26 rad/s |

The ROSbot motors are RotationalMotor nodes, each associated with a PositionSensor. They are named the following way:

| Wheel |	Motor name	| Position sensor name |
| --- | --- | --- | 
| Front right wheel	| front right wheel motor	| front right wheel motor sensor |
| Front left wheel	| front left wheel motor	| front left wheel motor sensor |
| Rear left wheel	| rear left wheel motor	| rear left wheel motor sensor |
| Rear right wheel	| rear right wheel motor	| rear right wheel motor sensor |

## RosBot.py

FAIRIS-Lite provides an easy-to-use Python class that streamlines the process of setting up your simulated 
environments. This is achieved by creating a class with a constructor that adds all the sensors and initializes 
them for use. We also provide setters and getters to easily access the sensors, motors, and cameras. Below we 
provide a full description of all attributes and class functions that are provided. 


# RosBot Python Class Documentation

The `RosBot` class provides a comprehensive interface for controlling and interacting with the Webots simulation environment for the RosBot robot. It offers various methods to manage motor velocity, read sensor values, interact with cameras, lidar, and other components, as well as control the simulation environment itself.

## Class Overview

This class inherits from the Webots `Supervisor` class and encapsulates functionalities for controlling the RosBot robot's movements, interacting with sensors, and managing simulation aspects.

### Import Statements

```python
from controller import Supervisor
from WebotsSim.libraries.RobotLib.Evironment import *
import matplotlib.pyplot as plt
```

### Class Definition

```python
class RosBot(Supervisor):
    ...
```

## Initialization

### `__init__(self)`

This constructor initializes an instance of the `RosBot` class, setting up various attributes, devices, and systems.

#### Usage

```python
rosbot = RosBot()
```

## Sensor Calibration

### `sensor_calibration(self)`

This method performs a single simulation timestep to update all sensors. It should be used during robot initialization and after teleporting the robot.

#### Usage

```python
rosbot.sensor_calibration()
```

## Compass Reading

### `get_compass_reading(self)`

This method reads the robot's IMU compass and returns the bearing in degrees. The bearing is calculated based on the compass's values, representing cardinal directions.

#### Usage

```python
bearing = rosbot.get_compass_reading()
```

## Encoder Readings

### `get_encoder_readings(self)`

This method reads the current encoder readings for all motors and returns an array of encoder positions.

#### Usage

```python
encoder_positions = rosbot.get_encoder_readings()
```

## Velocity Saturation

### `velocity_saturation(self, motor_velocity)`

This method caps the motor velocities to prevent PID calculations from exceeding motor speeds.

#### Usage

```python
saturated_velocity = rosbot.velocity_saturation(motor_velocity)
```

## Motor Velocity Control

The following methods allow you to set the velocity of individual motors:

- `set_front_left_motor_velocity(self, velocity)`
- `set_front_right_motor_velocity(self, velocity)`
- `set_rear_left_motor_velocity(self, velocity)`
- `set_rear_right_motor_velocity(self, velocity)`

Each of these methods sets the velocity of the corresponding motor to the specified value.

## Movement Control

- `stop(self)`: Sets all motors' speed to 0.
- `go_forward(self, velocity=1)`: Sets all motors' speed to the specified velocity.

## Sensor Readings

Methods to retrieve sensor readings:

- `get_front_left_motor_encoder_reading(self)`: Gets the current front-left motor encoder reading.
- `get_front_right_motor_encoder_reading(self)`: Gets the current front-right motor encoder reading.
- `get_rear_left_motor_encoder_reading(self)`: Gets the current rear-left motor encoder reading.
- `get_rear_right_motor_encoder_reading(self)`: Gets the current rear-right motor encoder reading.
- `get_front_left_distance_reading(self)`: Gets the current front-left distance sensor reading.
- `get_front_right_distance_reading(self)`: Gets the current front-right distance sensor reading.
- `get_rear_left_distance_reading(self)`: Gets the current rear-left distance sensor reading.
- `get_rear_right_distance_reading(self)`: Gets the current rear-right distance sensor reading.
- `get_lidar_range_image(self)`: Gets the Lidar range image, returns a list of 800 distances where the 0 index is at 
  the rear, 200 index is to the left, 400 index is to the front, and 600 index is to the right.

## Environment and Simulation Control

Methods for controlling the simulation environment:

- `load_environment(self, maze_file)`: Loads a maze from an XML file, creating walls, starting locations, and goal locations.
- `teleport_robot(self, x=0.0, y=0.0, z=0.0)`: Teleports the robot to the specified coordinates.
- `move_to_start(self)`: Moves the robot to a random starting position.
- `update_display(self, fig)`: Plots place cells and displays them on the simulation's display.

## Usage Example

Here is a basic usage example:

```python
# Changes Working Directory to be at the root of FAIRIS-Lite
import os
os.chdir("../..")

# Import MyRobot Class
from WebotsSim.libraries.MyRobot import MyRobot

# Create the robot instance.
robot = MyRobot()

# Loads the environment from the maze file
maze_file = 'worlds/mazes/Labs/Lab1.xml'
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
    robot.set_rear_left_motor_velocity(20)
    robot.set_rear_right_motor_velocity(20)
    robot.set_front_left_motor_velocity(20)
    robot.set_front_right_motor_velocity(20)

    # Calculates distance the wheel has turned since beginning of simulation
    distance_front_left_wheel_traveled = robot.wheel_radius * robot.get_front_left_motor_encoder_reading() / 1000

    # Stops the robot after the robot moves a distance of 1.5 meters
    if distance_front_left_wheel_traveled > 1.5:
        robot.stop()
        break
```

---

This documentation provides an overview of the `RosBot` class and its methods, allowing you to effectively control and interact with the Webots simulation environment for the RosBot robot.

# Extending the RosBot Class
Within FAIRIS-Lite, an additional Python class named MyRobot is available. This class is designed to build upon the 
functionalities of the RosBot class, offering further customization for your specific use cases. You can find the 
source code for this class in the file [FAIRIS-LITE/WebotsSim/libraries/MyRobot.py](MyRobot.py).

For smoother development, we recommend that you augment this class with your custom functions. Since MyRobot is 
derived from the RosBot class, all the functions detailed above will be at your disposal in this extended class. 
Moreover, you can introduce any additional functions tailored to your requirements. This approach ensures you 
leverage the existing capabilities while tailoring the robot's behavior to your needs.