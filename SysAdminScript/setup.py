from setuptools import find_packages, setup 

with open('README.md', 'r') as f: 
    long_description = f.read() 

setup( 
    name='SysAdminScript',
    version='0.1.0', 
    author='MikeTech93', 
    author_email='---', 
    description='A script for Linux SysAdmins to have a GUI based tool to perform simple daily tasks', 
    long_description=long_description, # This will be read from README.md file 
    long_description_content_type='text/markdown', # This will allow the file to be formatted correctly
    url='https://github.com/MYGITHUBURL/MYGITHUBREPOSITORY', 
    packages=find_packages('src') # This will enable all packages to be bundled correctly
) 
