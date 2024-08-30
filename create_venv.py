import os
import sys
import subprocess
import platform

def create_venv():
    try:
        subprocess.check_call([sys.executable, "-m", "venv", "venv"])
        print("Python virtual environment created successfully.")
    except subprocess.CalledProcessError:
        print("Unable to set up Python venv, exiting with ERROR:1")
        print("User may need to set up the Python venv separately.")
        sys.exit(1)

def add_fairis_to_path(project_path, venv_path):
    file_to_add_site_packages = os.path.join(venv_path, "site-packages", "FAIRIS_LIBS.pth")
    with open(file_to_add_site_packages, "w") as out_file:
        out_file.write(project_path)
    print(f"Added FAIRIS-Lite path to {file_to_add_site_packages}.")

def main():
    project_path = os.getcwd()
    print(f"Project Path: {project_path}")

    create_venv()

    venv_path = ""
    if platform.system() == 'Windows':
        venv_path = os.path.join("venv", "Lib")
    else:
        venv_path = os.path.join("venv", "lib", f"python{sys.version_info.major}.{sys.version_info.minor}")

    add_fairis_to_path(project_path, venv_path)

if __name__ == "__main__":
    main()
