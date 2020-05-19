from setuptools import setup, find_packages

setup(
    name='Pymodoro',
    description='A Python pomodoro clock',
    author='Jeff Moorhead',
    author_email='jeff.moorhead1@gmail.com',
    url='https://github.com/Jeff-Moorhead/pymodoro',
    packages=find_packages(),
    entry_points = {
        'console_scripts': ['pymodoro=pymodoro.__main__:main'],
    }
)
    
