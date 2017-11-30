# sitecustomize23
An implementation of sitecustomize.py that allows user to install their Python 2 and 3 packages outside of default directory.

System Requirements:

1) Either Python 2 or 3 is installed.

Optional System Requirements:
1) The following environment variables are created with the target directory as its value:

- PYTHONPATH (https://docs.python.org/2/using/cmdline.html#envvar-PYTHONPATH)
- PYTHONPATH2
- PYTHONPATH3

PYTHONPATH2 and PYTHONPATH3 are the folders to store the packages of Python 2 and Python 3 respectively.

Installation step:
There are 2 methods to use sitecustomize23.

The first method:
- Primarily for users with either 1 or exactly 2 versions of Python where one of which must be in Python 2.x series and the other must be in Python 3.x installed on their Windows PC. It allows the flexibility to store the modules anywhere as long as the path for both PYTHONPATH2 and PYTHONPATH3 are distinct (unique). When the value for both PYTHONPATH2 and PYTHONPATH3 are the same, it will fallback to the second method.

Please refer to the section 'Motivation' for the issues that leads to this restriction.


Step 1) Download sitecustomize.py into the path as per the value of PYTHONPATH.


The second method:
- It is intended for macOS (Formerly OS X) / Unix users who may face difficulites in setting global system envrionment variables especially when these settings are typically non-persistent (As in only valid when the shell is running) and might not be applicable for GUI applications.

- It is also intended for any user who installed multiple minor versions but same major of Python (I.e. Installing Python 2.6, Python 2.7 in the same system. This also applies to system that installed Python 3.5 and Python 3.6 etc.). 

The same issue described in the Motivation sections also applies here because Python modules (packages) supports different Python version by 'Minor' revision per Python Support Lifecycle (Refer to its Release Schedule, typically by Minor revision such as this for Python 3.6 series: https://www.python.org/dev/peps/pep-0494/)

Step 1) Download BOTH sitecustomize.py AND Installation.py into any folder, BUT the 2 files must be within the same folder.

Step 2) Open Command Prompt (Windows) / Terminal (Cygwin / Unix / macOS) and navigate to the downloaded directory using 'cd'

Example (Cygwin / Unix / macOS): cd ~/Downloads
Example (Windows): cd C:\User\username\Desktop

Step 3) Run the Installation.py by using each of the Python Minor release:
Example (Cygwin / Unix / macOS): 

python2.7 Installation.py
python3.6 Installation.py

Example (Windows):
C:\Python27\python.exe Installation.py
C:\Python36\python.exe Installation.py

Using this method, a DEFAULTPATH will be given for the following platforms to store Python Modules:

macOS: _/Applications/Python_Modules_

Windows (Excluding CygWin): _<System Drive>:\Python_Modules\python<Major.Minor>_
Example: _C:\Python_Modules\python3.6_
  
Unix (Including CygWin): _/opt/Python_Modules_


Usage:
After sitecustomize.py is downloaded onto PYTHONPATH, you may run either of the following to install the packages:

- By .tar.gz source:

_python<Major.Minor> setup.py install --prefix <PYTHONPATH2 / PYTHONPATH3 / DEFAULTPATH>_

Note for Windows user:
You may want to optionally create a shortcut with a name python<Major.Minor> in the folder where the respective python.exe is located in order for the above command to work.

Alternatively, you need to specify the exact path where the python.exe is located such as:

_C:\Python36\python setup.py install --prefix <PYTHONPATH2 / PYTHONPATH3 / DEFAULTPATH>_



- By wheel / PyPI:

_pip<Major.Minor> install <Path to Wheel file / package name> --prefix <PYTHONPATH2 / PYTHONPATH3 / DEFAULTPATH>_

Note 1: The prefix value in both scenarios should NOT contain the common path "Libs/site-packages".
Note 2: Append the correct Python Major.Minor version (2.7 / 3.3 / 3.4 / 3.5 / 3.6 etc.) as necessary after 'python' or 'pip'.

This implementation does not affect the ability to install via proxy.

Motivation:

I need a way to where one single folder can host the same dependency / module / packages for both Python 2 and Python 3. I have tried using --install-lib but Python may load the package from a wrong version instead and throws error.

Source: https://github.com/agronholm/pythonfutures/issues/69
