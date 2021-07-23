from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'An oven timer ding sound function to be called once your code finishes running!'

# Setting up
setup(
    name="ding",
    version=VERSION,
    author="Felipe Carraro Morita",
    author_email="<fmorita@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['python-vlc'],
    keywords=['python', 'ding', 'sound'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
