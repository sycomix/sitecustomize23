# sitecustomize23
An implementation of sitecustomize.py that allows user to install their Python 2 and 3 packages outside of default directory.

System Requirements:

1) Python 2 and 3 are installed.
2) The following environment variables are created with the target directory as its value:

- PYTHONPATH (https://docs.python.org/2/using/cmdline.html#envvar-PYTHONPATH)
- PYTHONPATH2
- PYTHONPATH3

PYTHONPATH2 and PYTHONPATH3 are the folders to store the packages of Python 2 and Python 3 respectively.

Installation step:
Download sitecustomize.py into the path where PYTHONPATH resides will do the job.

You will need to define the path for PythonPATH2 and PythonPATH3 so that this script will work. Otherwise, there will be no effects on the system.

Usage:
After sitecustomize.py is downloaded onto PYTHONPATH, you may run either of the following to install the packages:

- By .tar.gz source:
python.exe setup.py install --prefix <PYTHONPATH2 / PYTHONPATH3>

- By wheel / PyPI:
pip<2 / 3> install <Path to Wheel file / package name> --prefix <PYTHONPATH2 / PYTHONPATH3>

Note: The prefix value in both scenarios should NOT contain the common path "Libs/site-packages".

This implementation does not affect the ability to install via proxy.

Motivation:

I need a way to where one single folder can host the same dependency / module / packages for both Python 2 and Python 3. I have tried using --install-lib but Python may load the package from a wrong version instead and throws error.

Source: https://github.com/agronholm/pythonfutures/issues/69
