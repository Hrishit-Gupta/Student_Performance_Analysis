from setuptools import setup,find_packages
from typing import List
def get_requirements(file_str:str)->List[str] :
    '''
    this function returns the list of requirements
    '''
    requirements = []
    with open(file_str) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]


setup(
    name='ML project',
    author='Hrishit Gupta',
    version='0.0.1',
    package_dir=find_packages(),
    install_requires= ['numpy','pandas','seaborn']

)