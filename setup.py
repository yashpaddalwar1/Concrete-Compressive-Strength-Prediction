from setuptools import find_packages, setup
from typing import List

# Declaring Variables for Setup Function

PROJECT_NAME = "concrete-compressive-strength-prediction"
VERSION = "0.0.1"
AUTHOR = "Yash Ajit Paddalwar"
DESCRIPTION = "This is a concrete compressive strength predictor that predicts the strength of the cement"
PACKAGES = ['concrete']
REQUIREMENTS_FILE_NAME = 'requirements.txt'

def get_requirements_list() -> List[str]:

    """
        Description: This function gives the list of requirements mentioned in the requirements.txt file.
        Return: Returns a list of requirements mentioned in the requirements location.
    """

    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        return requirements_file.readlines().remove("-e .")

setup(
    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    packages = find_packages(),
    install_requires = get_requirements_list()
)

if __name__ == '__main__':
    print(get_requirements_list())