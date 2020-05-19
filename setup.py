from setuptools import setup, find_packages

setup(
    version='1.0.0',
    name='Pomodoropie',
    description='A Python pomodoro clock',
    author='Jeff Moorhead',
    author_email='jeff.moorhead1@gmail.com',
    url='https://github.com/Jeff-Moorhead/pomodoropie',
    packages=find_packages(),
    entry_points = {
        'console_scripts': ['pomodoropie=pomodoropie.__main__:main'],
    }
)
    
