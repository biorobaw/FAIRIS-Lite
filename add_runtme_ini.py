import os


def add_runtime_ini_to_dirs(controllers_dir, python_venv_path):
    for dirpath, dirnames, _ in os.walk(controllers_dir):
        for dirname in dirnames:
            dir_full_path = os.path.join(dirpath, dirname)
            runtime_ini_file = os.path.join(dir_full_path, "runtime.ini")

            with open(runtime_ini_file, "w") as out_file:
                out_file.write("[python]\n")
                out_file.write(f"COMMAND = {python_venv_path}")

            print(f"Added runtime.ini to {dir_full_path}")


def main():
    project_path = os.getcwd()
    python_venv_path = os.path.join(project_path, "venv", "bin", "python3")
    controllers_dir = os.path.join(project_path, "WebotsSim", "controllers")

    add_runtime_ini_to_dirs(controllers_dir, python_venv_path)


if __name__ == "__main__":
    main()
