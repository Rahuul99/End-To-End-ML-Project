from setuptools import setup, find_packages

def get_requirements():
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
    return requirements

setup(
    name='my_project',
    version='0.1',
    author='Rahul Mishra',
    packages=find_packages(),
    install_requires=get_requirements(),
    entry_points={
        'console_scripts': [
            'my_project=my_project.cli:main'
        ]
    }
)
