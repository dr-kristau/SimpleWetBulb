from setuptools import setup

setup(
    name='simplewetbulb',
    version='0.1.0',
    py_modules=['simplewetbulb'],
    install_requires=[
        'Click',
        'NumPy',
    ],
    entry_points={
        'console_scripts': [
            'simplewetbulb = simplewetbulb:cli',
        ],
    },
)
