from setuptools import setup, find_packages

#To create the dist we have to open a terminal at the package where the setup.py is and run python setup.py sdist and a folder will be created

setup(
    name='Messages',
    version='2.0',
    description='Package to say Hi and Bye',
    author='Myself',
    author_email='myself@hotmail.com',
    url='None',
    packages=find_packages(),
    scripts=['test.py'],
    install_requires=[package.strip() for package in open("requirements.txt").readlines()]      # Libraries that it needs example ['numpy>=2.2.5']
)