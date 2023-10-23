import sys
import os
import subprocess #To run command via Terminal.

try:
	currentDir = os.path.dirname(os.path.realpath(__file__))
	os.chdir(currentDir) #To set working directory as path of this installation script.

	sysVerText = str.format("{0}.{1}", sys.version_info.major, sys.version_info.minor)
	majorVer = int(sysVerText[0]) #To return only 2 or 3
	if (majorVer > 2):
		#Python 3.
		majorVer = 3
	else:
		#Python 2.
		majorVer = 2
		reload(sys)
		sys.setdefaultencoding("utf-8") #Tune for Python 2 to default as UTF-8 (N/A for Python 3).

	defaultPath = "" #Empty variable that will be assigned with a default Path.
	sysPlatform = sys.platform

	#Detect OS.
	if (sysPlatform == "darwin"):
		#Apple OSX. Not expected to support Classic Mac OS 9 or below. Expects using non-Apple shipped Python.
		defaultPath = str.format("/Library/Frameworks/Python.framework/Versions/{0}/lib/python{0}/site-packages/", sysVerText)
	elif (sysPlatform.startswith("win")):
		#Windows (Does not differentiate between NT-based such as Windows 2000 / XP and above or not).
		defaultPath = str.format("{0}\\Lib\\site-packages", sys.exec_prefix)
	else:
		#Other Unix including Cyginwin / Linux / FreeBSD etc.
		defaultPath = str.format("{0}/lib/python{1}/site-packages/", sys.exec_prefix, sysVerText)

	loadPath = "" #The path to load modules based on environment variable if possible.
	try:
		#Error always occur when environment variable is not set.
		loadPath = os.environ["PYTHONPATH"]
	except:
		#Given variable NOT set.
		loadPath = defaultPath

	#Converts given path into REAL PATH.
	source = os.path.realpath('sitecustomize.py')
	dest = os.path.realpath(loadPath)

	if (os.path.isdir(loadPath)):
		#If given path exists!
		command = []
		if (sysPlatform.startswith("win")):
			#For Windows, NEVER include the filename by providing a backslash so as to surpress prompt.
			command = ["xcopy", '/V', '/C', '/i', '/F', '/Y', '/Z', source, str.format("{0}\\", dest)]
		elif (sysPlatform == "darwin"):
			command = ["cp", source, dest]
		else:
			command = ["cp", '-d', source, dest]

		subprocess.call(command)
	else:
		#If Python is not installed or damaged installation!
		print("Unable to find the default path for storing Python Packages!\nPlease reinstall Python to fix this issue.")
except Exception as err:
	print(err)