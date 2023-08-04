# FAIRIS-Lite

FAIRIS-Lite is a project framework that allows you to implement navigational control logic directly on the open-source robotic simulation platform Webots. With this framework, you can create your own Webots controller without the need to set up a simulated environment or robot, as we provide all the materials required to get started.

## Requirements

To work with FAIRIS-Lite, ensure that your system meets the following requirements:

1. Python 3.9+: If you don't have Python 3.9 or above installed, you can find a guided tutorial on how to install or update Python [here](https://realpython.com/installing-python/) or [here](https://www.pythoncentral.io/how-to-update-python/).

2. Cyberbotics Webots R2023b: FAIRIS-Lite works in conjunction with Webots version R2023b. You need to install this open-source software to utilize FAIRIS-Lite. A guided installation guide can be found [here](https://cyberbotics.com/doc/guide/installation-procedure).

## Setup Instructions

Follow these steps to set up FAIRIS-Lite on your local machine:

1. Clone this repository onto your device.
2. Open a terminal session (on MacOS or Linux) or a command shell (on Windows).

### Launching Terminal on MacOS

1. Press Command + Space Bar on your Mac keyboard (alternatively, press F4).
2. Type "Terminal" in the Spotlight search and click to open the app.

### Launching Terminal on Linux

1. Press Ctrl+Alt+T to instantly launch a Terminal window.

### Launching Command Prompt on Windows

1. Press the Windows Key + R, type in `cmd.exe`, and press Enter.

![Run](https://www.majorgeeks.com/content/file/4355_ways%20to%20open%20the%20command%20prompt%20in%20windows%2011%201.jpg)

Once in the terminal session or command shell, navigate to the `setup` directory and run the following commands:

### MacOS and Linux
```shell
foo@bar: FAIRIS-Lite $ cd setup
foo@bar: setup $ python3 setup.py
```

### Windows
```shell
foo@bar: FAIRIS-Lite $ cd setup
foo@bar: setup $ python setup.py
```

Running the `setup.py` script will create a Python virtual environment (venv) and install all the necessary Python libraries to run FAIRIS-Lite. The script will also configure Webots so that any additional libraries created by the user can be imported and utilized.

## PyCharm Support

FAIRIS-Lite offers PyCharm integration with Webots. To set this up, follow these steps:

1. Open the FAIRIS-Lite directory as a project in PyCharm.
2. Add the content roots as the FAIRIS-Lite directory.
3. Set the Python interpreter to be the venv created in the previous steps.

For detailed instructions on configuring PyCharm to integrate with Webots, refer to the [guide](https://cyberbotics.com/doc/guide/using-your-ide#pycharm).

## Testing FAIRIS-Lite Setup

To test if FAIRIS-Lite has been set up properly, follow these steps:

1. Launch Webots and open the world file located in `FAIRIS-Lite -> WebotsSim -> worlds -> StartingWorld.wbt`.
2. Once Webots loads the world, you should see the Example controller running, which adds walls and places the robot in a starting location.
3. The robot will perform 8 actions, after which the simulation will reset.
4. By selecting the play button on the Webots interface, you will see this process repeat.

Now you have successfully set up FAIRIS-Lite, and you can start developing your robot controllers in Webots using Python. Happy coding!
