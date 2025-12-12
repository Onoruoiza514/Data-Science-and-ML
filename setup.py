from setuptools import find_packages, setup
from typing import List

hyphen_E_dot = "-e ."

def get_requirements(file_path: str) -> list[str]:
    """
    This function reads the requirements file and returns a list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if hyphen_E_dot in requirements:
            requirements.remove(hyphen_E_dot)

    return requirements

setup(
    name='Machine Learning Project',
    author='Abdulfaatihi',
    version='0.0.1',
    author_email='abdulfaatihitijani@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)