import subprocess
import os
import shutil
from fileallsearch import fileallsearch

appname = 'test'
pythonVersion = 'python3'

info_plist = """\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.1">
    <dict>
        <key>CFBundleExecutable</key>
        <string>core.py</string>
    </dict>
</plist>
"""

core_sh = """\
#!/bin/sh
SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
$SCRIPTPATH/venv/bin/python3 {runfile}
"""
core_py = """\
#!/usr/bin/python3
import subprocess
import sys

pythonV = sys.argv[0]
splt = pythonV.split('/')[:-1]
pythonV = '/'.join(splt)
cmd = f'{pythonV}/venv/bin/python3 {pythonV}/%s'
subprocess.run(cmd.split())
"""

def makedir():
    os.makedirs(f'./temp/{appname}.app/Contents/MacOS/',exist_ok=True)


def createVenv():
    subprocess.run(f'{pythonVersion} -m venv ./temp/{appname}.app/Contents/MacOS/venv'.split())


def runfile_copy(paths,runfile):
    for path in paths:
        shutil.copyfile(path,f'./temp/{appname}.app/Contents/MacOS/{path}')

    with open(f'./temp/{appname}.app/Contents/MacOS/core.py', 'w') as f:
        #f.write(core_py.format(runfile=runfile))
        f.write(core_py % runfile)

def rundir_copy(paths,runfile):                  
    print('rundir_copy',paths,runfile)
    shutil.copytree(paths,f'./temp/{appname}.app/Contents/MacOS/{paths}')
    with open(f'./temp/{appname}.app/Contents/MacOS/core.py', 'w') as f:
        f.write(core_py % runfile)


def install_lib(req_file):
    subprocess.run(f'./temp/{appname}.app/Contents/MacOS/venv/bin/pip3 install -r {req_file}'.split())


def set_Infoplist():
    with open(f'./temp/{appname}.app/Contents/Info.plist', 'w') as f:
        f.write(info_plist)



def set_permissions(paths):
    # FIXME: 全部する必要があるのかは謎
    for path in fileallsearch(f'./temp/{appname}.app/Contents/MacOS'):
        print(path)
        os.chmod(path,0o755)

    #os.chmod(f'./temp/{appname}.app/Contents/MacOS/venv',0o755)
    #os.chmod(f'./temp/{appname}.app/Contents/MacOS/core.sh',0o755)
    #for path in paths:
    #    os.chmod(f'./temp/{appname}.app/Contents/MacOS/{path}',0o755)
    

def main(runfile=None,paths=None,rundirectory=None,requirements=None):
    print(runfile,paths,rundirectory,requirements)
    if not runfile:
        raise Exception('runfile not found')
    makedir()
    print('makedir ok ')
    createVenv()
    print('create venv ok')
    if paths:
        runfile_copy(paths,runfile)
        print('runfile copy done!')
    elif rundirectory:
        rundir_copy(rundirectory,runfile)
        print('rundir copy done!')
    if requirements:
        install_lib(requirements)
        print('install lib done')
    else:
        print('requirements not found.')
    set_Infoplist()
    print('info priset done')
    set_permissions(paths)
    print('done!')


