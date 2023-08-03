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

	project_path = os.getcwd()
	print(project_path)
	file_to_add_site_packages = "venv/Lib/site-packages/FAIRIS_LIBS.pth"

	line_to_write = project_path

	with open(file_to_add_site_packages, "w") as out_file:
		out_file.write(line_to_write)
	subprocess.run(["setup\\windows_venv_setup.bat"])

	runtime_ini_file = "WebotsSim/controllers/Examples/runtime.ini"
	path_to_python_venv = project_path + "/venv/Scripts/python.exe"
	with open(runtime_ini_file, "w") as out_file:
		out_file.write("[python]\n")
		out_file.write("COMMAND = " + path_to_python_venv)

else:
	try:
		os.system("python3 -m venv venv")
	except:
		print("Unable to set up Python venv, exiting with ERROR:1")
		print("User may need to set up python vevn sepratly")
		sys.exit()

	project_path = os.getcwd()
	print(project_path)
	file_to_add_site_packages = "venv/lib/python3.9/site-packages/FAIRIS_LIBS.pth"

	line_to_write = project_path

	with open(file_to_add_site_packages, "w") as out_file:
		out_file.write(line_to_write)
	os.system("sudo chmod +x setup/unix_venv_setup.sh")
	subprocess.run(["setup/unix_venv_setup.sh"], shell=True)


	runtime_ini_file = "WebotsSim/controllers/Examples/runtime.ini"
	path_to_python_venv = project_path + "/venv/bin/python3.9"
	with open(runtime_ini_file, "w") as out_file:
		out_file.write("[python]\n")
		out_file.write("COMMAND = " + path_to_python_venv)

sys.exit()
