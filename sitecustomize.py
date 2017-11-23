import sys
import os
#Based on: https://stackoverflow.com/questions/16114391/adding-directory-to-sys-path-pythonpath
try:
	loadPath = os.environ['PythonPATH2'] #Get Python 2.
	if (sys.version_info > (3, 0)):
		loadPath = os.environ['PythonPATH3'] #IF Python 3.
	else:
		sys.setdefaultencoding("utf-8") #Tune for Python 2 to default as UTF-8 (N/A for Python 3).

	os.environ['PythonPATH'] = loadPath #Current PythonPATH is only useful to load this file, and nothing else.
	parentFolder = loadPath.split(os.sep)[-2] #The previous folder name.
	if (parentFolder != "Lib"):
		loadPath = os.path.join(loadPath, "Lib")

	currentFolder = loadPath.split(os.sep)[-1] #The current folder name.
	if (currentFolder != "site-packages"):
		loadPath = os.path.join(loadPath, "site-packages")

	#Using --prefix must have a value that end with '\Lib\site-packages' regardless of OS.
	sys.path.insert(0,loadPath) #Prioirtize this folder to load the binaries.

	#Adapted from: https://pymotw.com/2/site/
	import site
	site.addsitedir(loadPath)

	if (not os.path.isdir(loadPath)):
		os.makedirs(loadPath) #Automatically create folder if necessary.
except:
	pass
