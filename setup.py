"""
setup.py

Purpose:
    This script facilitates the packaging of the system. 
    It reads the project metadata, requirements, and classifiers to generate a distributable package.
"""

from setuptools import find_packages, setup
from typing import List

# Get long description from the readme file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "rubles"
AUTHOR_USER_NAME = "etietopabraham"
SRC_REPO = "rubles"
AUTHOR_EMAIL = "etietopdemas@gmail.com"

def get_requirements(file_path: str) -> List[str]:
    """
    Retrieves the list of requirements from the specified file.

    Args:
    - file_path (str): Path to the requirements file.

    Returns:
    - List[str]: List of requirements.
    """
    with open(file_path, 'r') as file:
        # Exclude lines with '-e .' as it's commonly used to indicate editable installs
        requirements = [line.strip() for line in file if line.strip() != "-e ."]
    return requirements

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Rubles fintech app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"" : "src"},
    packages=find_packages(where="src"),
    classifiers=[  
        "Programming Language :: Python :: 3.10.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10.10',
    install_requires=get_requirements('requirements.txt')
)