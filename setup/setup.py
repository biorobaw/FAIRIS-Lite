import os
import subprocess
import platform
import sys

os.chdir("../")

if platform.system() == 'Windows':
	try:
		os.system("python -m venv venv")
	except:
		print("Unable to set up Python venv, exiting with ERROR:1")
		print("User may need to set up python vevn sepratly")
		sys.exit()

	subprocess.run(["setup\\windows_venv_setup.bat"])
else:
	try:
		os.system("python3 -m venv venv")
	except:
		print("Unable to set up Python venv, exiting with ERROR:1")
		print("User may need to set up python vevn sepratly")
		sys.exit()

	subprocess.run(["setup/unix_venv_setup.sh"], shell=True)

project_path = os.getcwd()
print(project_path)
file_to_add_site_packages = "venv/lib/python3.9/site-packages/FAIRIS_LIBS.pth"

line_to_write = project_path

with open(file_to_add_site_packages, "w") as out_file:
	out_file.write(line_to_write)
os.system("sudo chmod +x setup/unix_venv_setup.sh")



sys.exit()
