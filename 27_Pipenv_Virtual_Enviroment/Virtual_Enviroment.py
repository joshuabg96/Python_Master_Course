"""
pipenv install : Create a new virtual enviroment

After install you will see a path, for example:
Virtualenv location:  C:\Users\josue\.virtualenvs\New_Env-Lb1o967a
Here you will have the copy of python that you are going to use in your project

pipenv --py: See the path where all the enviroment is set

pipenv shell: Activate the virtual enviroment in the cmd to make installation for the enviroment
exit: To exit the virtual enviroment

pipenv run [command]: Run a comman in the virtual enviroment, this only applies for the command, all the command next to it will be out of the enviroment

pipenv install [packages]: Install packages for all the user, dev and final user

pipenv install [packages] --dev: Install for developer version, not for final user

pipenv install [packages]==[version]: Install a specific version of the package updgrade or downgrade

pipenv unistall [package]: unistall the package of the enviroment

pipenv check: Check requirements and safety of the packages

pipenv --rm: Remove the virtual enviroment (Not delete the files)

pipenv install: Recover the virtual enviroment if we have the files (but dev dependencies are not installed)

pipenv install --dev: Install the virtual enviroment dev version

"""

import sys

print(sys.executable)       # Python interpreter

