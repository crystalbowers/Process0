I created a new python3.7 virtual environment in the motorcode directory. The name of the folder that the virtual environment lives in is called 'env'.

This environment allows you to run Python 3.7 and install packages without affecting the main Python 3.6 installation on your system, while keeping any package or Python-related problems within the environment.

I already created an environment, but to recreate on in case any problems occur:

cd ~/Documents/mechanical/motorcode
sudo rm -r env
python3.7 -m venv env

To activate the virtual environment:

cd ~/Documents/mechanical/motorcode
source env/bin/activate

You will see '(env)' before your path and username in the terminal, which indicates that the virtual environment is active. Now you can run your files as usual. This is using the python and pip (3.7) in the virtual env, not the base system ones (3.6):

python test.py
pip install requests

To deactivate the virtual environment, simply type:

deactivate

When adding new packages, make sure to activate the virtual environment first. You can add packages by using 'pip install x', but we recommend adding them to your requirements.txt file on your laptop, committing and pushing the changes to GitHub, and then running the following command on the Jetson:

git pull
pip install -r requirements.txt

Note: Make sure to activate the virtual environment before installing requirements!

To add a new package to your requirements.txt file, just add a new line with the package name, e.g., 'Cool-Package'.

If you want to pip install packages on your laptop and auto-generate a requirements.txt file, you can run the following command:

pip freeze > requirements-new.txt

Please note that if there is a package that does not work on your laptop (e.g., Jetson.GPIO), it will not be included in the generated file. All installed packages will be listed in a file called requirements-new.txt.
