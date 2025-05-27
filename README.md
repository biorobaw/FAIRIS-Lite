Here is the full raw Markdown content for the updated `README.md`:

````markdown
# FAIRIS-Lite

FAIRIS-Lite is a project framework that allows you to implement navigational control logic directly on the open-source robotic simulation platform Webots. With this framework, you can create your own Webots controller without the need to set up a simulated environment or robot, as we provide all the materials required to get started.

---

## Requirements

To work with FAIRIS-Lite, ensure that your system meets the following requirements:

### 1. Python 3.10+

#### **Windows Users**:
- **Important**: It’s crucial to install Python 3.10+ from the Microsoft Store to avoid potential issues with PATH configurations and permissions.
- **Installation Instructions**:
  1. Open the **Microsoft Store** on your Windows PC.
  2. In the search bar, type **"Python 3.10"**.
  3. Select **Python 3.10** from the list of results.
  4. Click **Get** or **Install** to download and install Python 3.10 on your machine.
     - [Microsoft Store Python 3.10](https://docs.microsoft.com/en-us/windows/images/store-install-python.png)  

  5. Once installed, verify the installation by opening Command Prompt and typing:
  
   ```shell
   python3 --version
````

* This should return `Python 3.10.x` or higher if installed correctly.

#### **Linux Users**:

* **Ensure you have Python 3.10+ installed.** Most distributions can install it using the package manager:

  ```shell
  sudo apt-get install python3.10
  ```

### 2. Cyberbotics Webots R2025a

FAIRIS-Lite works in conjunction with Webots version R2025a. Ensure you install Webots correctly:

#### **Linux Users**:

* **Do not install Webots from the Snap packaging** due to known compatibility issues. Instead, use the `.deb`
  package or tarball for installation.
* **Installation Instructions**:

  * Follow the detailed installation guide [here](https://cyberbotics.com/doc/guide/installation-procedure#installation-on-linux).

#### **Windows and macOS Users**:

* Download and install Webots R2023b from the official [Cyberbotics website](https://cyberbotics.com/#download).

### 3. Git

Ensure that you have Git installed to clone the FAIRIS-Lite repository:

* **Windows**: Download and install Git from [git-scm.com](https://git-scm.com/download/win).

* **Linux**: Install Git via your package manager:

  ```shell
  sudo apt-get install git
  ```

* **macOS**: Install Git via Homebrew:

  ```shell
  brew install git
  ```

---

## Setup Instructions

Follow these steps to set up FAIRIS-Lite on your local machine:

### 1. Clone the Repository

Clone this repository onto your device. There are numerous ways to achieve this, and you can decide which option is best for you. If you plan to use this repo for a course or an extended period, we recommend that you clone the repo and perform pulls when an update is pushed. A complete guide on how to clone GitHub repositories can be found [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

**Clone command:**

```shell
git clone https://github.com/biorobaw/FAIRIS-Lite.git
```

### 2. Run the Setup Script

Run the provided setup script to configure the project. This script:

* Searches for Python 3.12+ (falls back to 3.11/3.10 if needed)
* Creates a Python virtual environment
* Adds the FAIRIS-Lite root directory to the Python path
* Automatically generates `runtime.ini` files in all controller directories

```shell
python3 create_venv.py
```

You should see output indicating that the venv was created and that the `runtime.ini` files were added.

### 3. Activate Python Virtual Environment

After creating the virtual environment, you need to activate it before using the FAIRIS-Lite packages.

#### **Windows**:

```shell
venv\Scripts\activate
```

#### **macOS/Linux**:

```shell
source venv/bin/activate
```

You should now see your terminal prompt change to indicate that the virtual environment is active (e.g., `(venv)` at the start of your command line).

---

### 4. Install Required Python Packages

With the virtual environment activated, install all necessary dependencies using:

```shell
pip install -r requirements.txt
```

This will install all libraries needed for your Python Virtual environment to run FAIRIS-Lite in Webots.

---
## Updating Runtime Configurations for New Controllers

If you create a **new controller directory** under `WebotsSim/controllers/`, you will need to **re-run** the `add_runtime_ini.py` script to generate the appropriate `runtime.ini` file for that new controller:

```shell
python3 add_runtime_ini.py
```

This ensures that Webots knows to use the correct Python interpreter from your virtual environment.

### Example Directory Structure for Manual Configuration

Here’s an example structure showing where to place the `runtime.ini` files:

```
FAIRIS-LITE/
├── WebotsSim/
│   ├── controllers/
│   │   ├── template/
│   │   │   ├── template.py
│   │   │   ├── runtime.ini  # Manually created
│   │   ├── my_controller/
│   │   │   ├── my_controller.py
│   │   │   ├── runtime.ini  # Manually created
│   └── ...other WebotsSim files...
├── fairis_tools/
│   ├── __init__.py
│   ├── my_robot.py
│   └── ...other modules students can use...
├── fairis_lib/
│   ├── __init__.py
│   ├── environment_loader.py
│   └── ...other foundational modules...
├── setup.py
└── README.md
```
---

## PyCharm Integration (Optional)

FAIRIS-Lite supports PyCharm integration with Webots. Follow these steps to set it up:

1. Open the FAIRIS-Lite directory as a project in PyCharm.
2. Set the Python interpreter to the virtual environment created earlier.
3. Ensure the project structure includes the `fairis_tools` and `fairis_lib` directories.

For detailed instructions on configuring PyCharm with Webots, refer to this [guide](https://cyberbotics.com/doc/guide/using-your-ide#pycharm).

---

## Testing the Setup

To ensure FAIRIS-Lite is set up correctly:

1. Launch Webots and open the world file located at `FAIRIS-Lite/WebotsSim/worlds/StartingWorld.wbt`.
2. Verify that the Template controller is running, which should add walls and place the robot in a starting location.
3. The robot should print sensor readings and move approximately 1.5 meters before stopping.
4. Use the reset button in the Webots interface to see this process repeat.

If everything works as expected, you’re ready to start developing your robot controllers in Webots using Python.

---

## Additional Documentation

- **Guide for Webots Controller Creation**: Detailed instructions for creating a new Webots Robot Controller can be found [here](WebotsSim/controllers/README.md).
- **`HamBot` Library Documentation**: The `HamBot` class, which provides functions to access sensors, motors, and load 
  objects in the simulated environment, is documented [here](fairis_tools/README.md).
