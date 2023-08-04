# FAIRIS-Lite
This repo is a project framework that allows people to directly implement navigational control logic on the open source robotic simulation  (Webots). This framework enables users to create their on webots controller without the need to set up a simulated environment or robot with in webots, as we provide all the materials needed to get started.

# Requirements

FAIRIS-Lite is built with the intention of developing robot controllers in python. As such, your system will require Python3.9+. If your system does not have python3.9 or above installed on your, you will need to do so. A guided tutorial on how to install or update Python is provided here: [install](https://realpython.com/installing-python/) or [update](https://www.pythoncentral.io/how-to-update-python/).

FAIRIS_Lite works in conjunction with Cyberbotics's Webots and supports version R2023b. You will need to install this open-source software inorder to utilize FAIRIS-Lite. A guided instalation guide can be found [here](https://cyberbotics.com/doc/guide/installation-procedure).

# Setup Instructions

Once you you have ensured that your system meets the needed requirements, you will need to clone this repo onto your device. Once FAIRIS-Lite is on your local machine you will need to open a terminal session (om MacOS or Linux) or a command shell (Windows).

## Launching terminal on MacOS

1. Press Command + Space Bar on your Mac keyboard (alternatively, press F4)
2. Type in “Terminal”
3. When you see Terminal in the Spotlight search list, click it to open the app.

## Launching terminal on Linux

1. Pressing Ctrl+Alt+T will instantly launch a Terminal window at any moment. The GNOME Terminal window will immediately appear.

## Launching command sheel on Windows

1. Press the Windows Key + R, type in cmd.exe, and press Enter.

![RUN.](https://www.majorgeeks.com/content/file/4355_ways%20to%20open%20the%20command%20prompt%20in%20windows%2011%201.jpg)

## Setup commands

Once in a terminal session or command shell, you will need to run the command listed below. Note, You may be required to type your user password to enable permissions to executable files. 

### MacOS and Lunix
```shell
foo@bar: FAIRIS-Lite $ cd setup
foo@bar: setup $ python3 setup.py

```

### Windows
```shell
foo@bar: FAIRIS-Lite $ cd setup
foo@bar: setup $ python setup.py

```

Running the the python script setup.py, a python virtual environment, called venv, will be created as well installing all of the needed python libraries to run FAIRIS-Lite. This script will also configre Webots so that all additional libraries created by the user can be imported and utilized by webots. 

# PyCharm Support

FAIRIS-Lite supports PyCharm integration with Webots. To set this up you will need to open the FAIRIS-Lite directory as a project in PyCharm and add the content roots as the FAIRIS-Lite directory. You will also need to set the Python interprature to be the venv created  in the steps above.

Finally, you will also need to configure PyCharm in integrate with Webots. A detailed guide can be found [here](https://cyberbotics.com/doc/guide/using-your-ide#pycharm).

# Testing FAIRIS-Lite setup

To test if FAIRIS-Lite has been setup properly, you will need to launch Webots and open the world file located in FAIRIS-Lite -> WebotsSim -> worlds -> StartingWorld.wbt. Once Webots loads the world you should see that the Example controller is running, which will add walls and place the robot is a location to start at. The robot should them preform 8 actions, after which the simulation will reset. By selecting the play button on the Webots interface you will see this process repeat. 


