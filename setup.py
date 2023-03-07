from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will retuwn the list of requiements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='tej',
author_email='kirantej486@gmail.com',
packages=find_packages(),
# install_requires=['pandas','numpy','seaborn']
# not feasible to write all the packages required for the project
install_requires=get_requirements('requirements.txt')
)

