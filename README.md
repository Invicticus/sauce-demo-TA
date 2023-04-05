# sauce-demo-TA
** QA challenge issued to my by RealDecoy **

# **Project Description**

This project was created based on a challenge issued by RealDecoy. In this project you will find test files created using python, driven by selnium web driver and pytest. Below I will detail steps on how to run the web automation project.

**Steps to run project**

Repository Branches
master contains the README but no code
The <> contains the test code used to drive the web automation.

Python Setup
This course requires Python 3.11.2. You can download the latest Python version from Python.org and follow the appropriate installation instructions for your operating system.

Python Installation and Tools
You can complete this web automation using any OS: Windows, macOS, Linux, etc.

You should also have a good Python editor/IDE. Good choices include PyCharm and Visual Studio Code.

You will also need Git if you want to clone this repository locally. 

This file will use a handful of third-party packages:

pytest
pytest-cov
pytest-html
pytest-xdist
requests
These packages are not part of Python's standard library. They must be installed separately using pip, the standard Python package installer.

To install each package, enter pip install <package-name> at the command line. For example: pip install pytest. If you already have a package installed but need to upgrade its version, run pip install --upgrade <package-name>.

Please note that if you need to use the python3 command to run Python, then you might also need to use the pip3 command in lieu of pip.

Running Tests
To run the example tests from the command line, run python -m pytest from the project root directory. This command will discover and run all tests in the project.

You can also run tests using the shorter pytest command. However, I recommend always using the lengthier python -m pytest command. The lengthier command automatically adds the current directory to sys.path so that all modules in the project can be discovered.

The pytest command has several command line options. Course material will cover many of them. Check out the Usage and Invocations page for complete documentation.


