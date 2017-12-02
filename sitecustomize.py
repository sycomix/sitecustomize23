import sys
import os
import tempfile

#Check whether if file system is case sensitive or not.
#Source: https://stackoverflow.com/questions/7870041/check-if-file-system-is-case-insensitive-in-python
def is_fs_case_sensitive():
	if not hasattr(is_fs_case_sensitive, 'case_sensitive'):
		with tempfile.NamedTemporaryFile(prefix='TmP') as tmp_file:
			setattr(is_fs_case_sensitive,
					'case_sensitive',
					not os.path.exists(tmp_file.name.lower()))

	return (is_fs_case_sensitive.case_sensitive)

#Based on: https://stackoverflow.com/questions/16114391/adding-directory-to-sys-path-pythonpath
try:
	sysVerText = str.format("{0}.{1}", sys.version_info.major, sys.version_info.minor)
	majorVer = int(sysVerText[0]) #To return only 2 or 3
	oppo = 2 #To return the opposite version of majorver.

	if (majorVer > 2):
		#Python 3.
		majorVer = 3
		oppo = 2
	else:
		#Python 2.
		majorVer = 2
		oppo = 3
		reload(sys)
		sys.setdefaultencoding("utf-8") #Tune for Python 2 to default as UTF-8 (N/A for Python 3).

	defaultPath = "" #Empty variable that will be assigned with a default Path.
	endPath = [] #The standard set of folders in the level under prefix.
	sysPlatform = sys.platform

	#Detect OS.
	if (sysPlatform == "darwin"):
		#Apple OSX. Not expected to support Classic Mac OS 9 or below.
		defaultPath = "/Applications/Python_Modules"
		endPath.append("lib")
		endPath.append(str.format("python{0}", sysVerText))
		endPath.append("site-packages")
	elif (sysPlatform.startswith("win")):
		#Windows (Does not differentiate between NT-based such as Windows 2000 / XP and above or not).
		drive = os.path.splitdrive(sys.executable)[0] #Determines which drive hosts booting OS.
		defaultPath = str.format("{0}\\Python_Modules\\python{1}", drive, sysVerText)
		endPath.append("Lib")
		endPath.append("site-packages")
		#Note: In Windows, Python 2 and 3 typically installed in distinct folder.
		#However, Unix generally installs python 2 and python 3 executable in same folder.
	else:
		#Other Unix including Cyginwin / Linux / FreeBSD etc.
		defaultPath = "/opt/Python_Modules"
		endPath.append("lib")
		endPath.append(str.format("python{0}", sysVerText))
		endPath.append("site-packages")

	loadPath = "" #The path to load modules based on environment variable.
	oppoPath = "" #The path where the other major version of Python Modules will be installed to.
	envNameParent = "PYTHONPATH" #Always Case sensitive for environment variable.

	try:
		#Error always occur when environment variable is not set.
		loadPath = os.environ[str.format("{0}{1}", envNameParent, majorVer)]
		try:
			oppoPath = os.environ[str.format("{0}{1}", envNameParent, oppo)]
		except:
			pass

		if (oppoPath != ""):
			#Do not compare when oppoPath is blank.
			#In any case, os.path.realpath may try to take relative path of Current Working Directory if absolute path is not defined.
			if ((loadPath == oppoPath) or ((is_fs_case_sensitive() and loadPath.lower()) == oppoPath.lower())):
				#Revert to default value when PYTHONPATH 2 and PYTHONPATH3 are same address.
				raise Exception("PYTHONPATH2 and PYTHONPATH3 should NOT be the same value!")

	except:
		#Given variable NOT set.
		loadPath = defaultPath

	endCount = len(endPath) #To calculate number of folder levels used after prefix.
	countDown = endCount #Countdown towards 0.

	for f in range(endCount):
		folder = endPath[f]
		parentFolder = loadPath.split(os.sep)[(countDown * -1)] #The folder name at f level above.
		if ((parentFolder != folder) or (is_fs_case_sensitive() and parentFolder.lower() != folder.lower())):
			#If case sensitive fail OR when case insensitive also fail, then join the path.
			loadPath = os.path.join(loadPath, folder)

		countDown -= 1 #Proceed to next folder to compare.

	#Using --prefix must have a value that end with '\Lib\site-packages' in Windows OR /lib/python<VerMajor><verMin>/site-packages in Unix.
	sys.path.insert(0,loadPath) #Prioirtize this folder to load the binaries.

	#Adapted from: https://pymotw.com/2/site/
	import site
	site.addsitedir(loadPath)

	#Automatically creates folder if necessary.
	if (not os.path.isdir(loadPath)):
		os.makedirs(loadPath) #Takes care of case sensitiveness.
except:
	pass