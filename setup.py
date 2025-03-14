from setuptools import setup,find_packages
from typing import List
HYPEN_DOT_E = "-e ."
def get_requirements(file_str:str)->List[str] :
    '''
    this function returns the list of requirements
    '''
    requirements = []
    with open(file_str) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)

    return requirements

setup(
    name='ML project',
    author='Hrishit Gupta',
    version='0.0.1',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
    
)