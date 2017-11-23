import sys
import os
#Based on: https://stackoverflow.com/questions/16114391/adding-directory-to-sys-path-pythonpath
boolPython2 = True #Assume Python 2 only.
loadPath = os.environ['PythonPATH2']
if (sys.version_info > (3, 0)):
	loadPath = os.environ['PythonPATH3'] #IF Python 3.

os.environ['PythonPATH'] = loadPath
sys.path.insert(0,loadPath)

#Adapted from: https://pymotw.com/2/site/
import site
site.addsitedir(loadPath)