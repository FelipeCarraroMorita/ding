from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'An oven timer dingsound sound function to be called once your code finishes running!'

# Setting up
setup(
    name="dingsound",
    version=VERSION,
    author="Felipe Carraro Morita",
    author_email="<fmorita@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['playsound', 'IPython'],
    keywords=['python', 'dingsound', 'sound'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
