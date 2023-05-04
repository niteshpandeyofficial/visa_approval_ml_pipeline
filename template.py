import os
import sys
from pathlib import Path
import logging

while True:
    project_name=input('Enter Your Project Name:')
    if project_name!='':
        break


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s:%(levelname)s] %(message)s"
)
list_of_file=[
    f"{project_name}/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/component/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"config/config.yaml",
    f"setup.py",
    f"main.py",
    f"requirements.txt"
]

for file_path in list_of_file:
    file_path=Path(file_path)
    filedir,filename=os.path.split(file_path)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating new directory at :{filedir} for file {filename}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,'w') as f:
            pass
        logging.info(f"Creating a new file: {filename} for path: {file_path}")
    else:
        logging.info(f"file is already present at: {file_path}")
