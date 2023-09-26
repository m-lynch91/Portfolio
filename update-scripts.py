from pathlib import Path
from datetime import datetime
import sys
import shutil
import os

'''
Program:    update-script.py
Purpose:    copies .bat files from a python code repo over to user home directory so that
            scripts can be run from Windows Run
Author:     Mike Lynch
'''

pythonDir = Path('C:\\Users\\miche\\source\\repos\\PythonRepo\\PythonLearning')
scriptDir = Path.home()

# lists all the .bat files in the python-repo
pythonDirScripts = list(pythonDir.glob('*.bat'))
scriptDirScripts = list(scriptDir.glob('*.bat'))

if len(sys.argv) == 2 and sys.argv[1].lower() == 'list':
    print('List of python scripts in PythonLearning:')
    # print(pprint.pformat(pythonDirScripts))
    for i in pythonDirScripts:
        scriptName = i.name
        dateModified = str(datetime.fromtimestamp(os.path.getmtime(i)))
        print(f'Script name: {scriptName:<{len(dateModified)+5}} Date modified: {dateModified}')

    print('Number of scripts in PythonLearning: ' + str(len(pythonDirScripts)))

    print('\nList of python scripts in User Home Directory (' + Path.home().absolute().name + ')')
    # print(pprint.pformat(scriptDirScripts))
    for i in scriptDirScripts:
        scriptName = i.name
        dateModified = str(datetime.fromtimestamp(os.path.getmtime(i)))
        print(f'Script name: {scriptName:<{len(dateModified)+5}} Date modified: {dateModified}')

    print('Number of scripts in User Home Directory: ' + str(len(scriptDirScripts)))
    print('\n')


# move all .bat files from pythonDir to scriptDir
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'update':
    for file in pythonDirScripts:
        shutil.copyfile(file.absolute(), scriptDir / file.name)
    print('Scripts copied to ' + str(scriptDir.absolute()))

# TODO: accept command line arguments such that user can specify dir to move scripts to