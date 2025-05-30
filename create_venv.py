import os
import sys
import subprocess
import platform


def find_python_version():
    preferred_order = ["python3.12", "python3.11", "python3.10", "python3"]

    for executable in preferred_order:
        try:
            version_output = subprocess.check_output([executable, "--version"], stderr=subprocess.STDOUT)
            version_str = version_output.decode("utf-8").strip().split()[1]
            version_tuple = tuple(map(int, version_str.split('.')))

            if version_tuple >= (3, 10):
                print(f"Using Python executable: {executable} (version {version_str})")
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


def add_fairis_to_path(project_path):
    if platform.system() == "Windows":
        site_packages_dir = os.path.join("venv", "Lib", "site-packages")
    else:
        python_bin = os.path.join("venv", "bin", "python3")
        if not os.path.exists(python_bin):
            python_bin = os.path.join("venv", "bin", "python")  # fallback

        try:
            version_output = subprocess.check_output([python_bin, "--version"], stderr=subprocess.STDOUT)
            version_str = version_output.decode("utf-8").strip().split()[1]
            version_tag = f"python{'.'.join(version_str.split('.')[:2])}"
        except Exception as e:
            print(f"Failed to detect venv Python version: {e}")
            sys.exit(1)

        site_packages_dir = os.path.join("venv", "lib", version_tag, "site-packages")

    if not os.path.exists(site_packages_dir):
        print(f"ERROR: Could not find site-packages directory: {site_packages_dir}")
        sys.exit(1)

    pth_file_path = os.path.join(site_packages_dir, "FAIRIS_LIBS.pth")
    with open(pth_file_path, "w") as out_file:
        out_file.write(project_path)
    print(f"Added FAIRIS-Lite root to {pth_file_path}.")


def run_runtime_ini_setup():
    try:
        import add_runtime_ini
        add_runtime_ini.main()
    except ImportError as e:
        print(f"ERROR: Failed to import add_runtime_ini.py: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: add_runtime_ini.py failed to run: {e}")
        sys.exit(1)


def main():
    project_path = os.getcwd()
    print(f"Project Path: {project_path}")

    python_executable = find_python_version()
    create_venv(python_executable)
    add_fairis_to_path(project_path)
    run_runtime_ini_setup()


if __name__ == "__main__":
    main()
