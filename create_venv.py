import os
import sys
import subprocess
import platform


def find_python_version():
    # List of potential Python executables to check
    python_executables = ["python3.10", "python3.11", "python3.12", "python3"]

    for executable in python_executables:
        try:
            # Check if the Python executable is available
            version_output = subprocess.check_output([executable, "--version"], stderr=subprocess.STDOUT)
            version_str = version_output.decode("utf-8").strip().split()[1]
            version_tuple = tuple(map(int, version_str.split('.')))

            # Use this executable if it is version 3.10 or higher
            if version_tuple >= (3, 10):
                return executable
        except (subprocess.CalledProcessError, FileNotFoundError):
            continue

    print("No suitable Python 3.10+ executable found, exiting with ERROR:1")
    sys.exit(1)


def create_venv(python_executable):
    try:
        subprocess.check_call([python_executable, "-m", "venv", "venv"])
        print(f"Python virtual environment created successfully with {python_executable}.")
    except subprocess.CalledProcessError:
        print("Unable to set up Python venv, exiting with ERROR:1")
        sys.exit(1)


def add_fairis_to_path(project_path, venv_path):
    file_to_add_site_packages = os.path.join(venv_path, "site-packages", "FAIRIS_LIBS.pth")
    with open(file_to_add_site_packages, "w") as out_file:
        out_file.write(project_path)
    print(f"Added FAIRIS-Lite path to {file_to_add_site_packages}.")


def main():
    project_path = os.getcwd()
    print(f"Project Path: {project_path}")

    python_executable = find_python_version()
    create_venv(python_executable)

if __name__ == "__main__":
    main()
