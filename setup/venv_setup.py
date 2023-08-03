import os
import sys


project_path = os.getcwd()
print(project_path)

os.system("python3 -m pip install tensorflow numpy scikit-learn scipy matplotlib astar pandas torch")

file_to_add_site_packages = "venv/lib/python3.9/site-packages/FAIRIS_LIBS.pth"

line_to_write = project_path

with open(file_to_add_site_packages, "w") as out_file:
	out_file.write(line_to_write)

print("Successfully set up Python3.9 venv for Webots!")
print("Press Enter to finish.")

sys.exit()


