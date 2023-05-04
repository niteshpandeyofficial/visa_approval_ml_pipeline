from setuptools import setup,find_packages
from distutils.core import setup
from typing import List

PROJECT_NAME='Machine Learning End To End Project'
VERSION="0.0.1"
AUTHOR="Nitesh Pandey"
DESCRIPTION="This is complete end to end machine learning project"


HYPHEN_E_DOT="-e ."
def get_requirements_list():
    with open('requirements.txt','r') as req_file:
        req_list=req_file.readlines()
        req_list=[req_name.replace("\n","") for req_name in req_list]
        if HYPHEN_E_DOT in req_list:
            req_list.remove(HYPHEN_E_DOT)
        return req_list


setup(
    name=PROJECT_NAME,
    author=AUTHOR,
    version=VERSION,
    description=DESCRIPTION,
    author_email='niteshpandeyofficial@gmail.com',
    packages=find_packages(), 
    install_requires=get_requirements_list()
    )