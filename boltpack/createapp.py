import subprocess
import os
import shutil

appname = 'test'
pythonVersion = 'python3'

info_plist = """
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.1">
    <dict>
        <key>CFBundleExecutable</key>
        <string>core.sh</string>
    </dict>
</plist>
"""

core_sh = """
#!/bin/sh
SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
$SCRIPTPATH/venv/bin/python3 {runfile}
"""

def makedir():
    os.makedirs(f'./temp/{appname}.app/Contents/MacOS/',exist_ok=True)


def createVenv():
    subprocess.run(f'{pythonVersion} -m venv ./temp/{appname}.app/Contents/MacOS/venv'.split())


def runfile_copy(paths,runfile):
    for path in paths:
        shutil.copyfile(path,f'./temp/{appname}.app/Contents/MacOS/{path}')

    with open(f'./temp/{appname}.app/Contents/MacOS/core.sh', 'w') as f:
        f.write(core_sh.format(runfile=runfile))


def install_lib(req_file):
    subprocess.run(f'./temp/{appname}.app/Contents/MacOS/venv/bin/pip3 install -r {req_file}'.split())


def set_Infoplist():
    with open(f'./temp/{appname}.app/Contents/Info.plist', 'w') as f:
        f.write(info_plist)



def set_permissions(paths):
    os.chmod('./temp/{appname}.app/Contents/MacOS/venv',0o775)
    os.chmod('./temp/{appname}.app/Contents/MacOS/core.sh',0o775)
    for path in paths:
        os.chmod(f'./temp/{appname}.app/Contents/MacOS/{path}',0o775)
    

def main(paths,runfile):
    makedir()
    print('makedir ok ')
    createVenv()
    print('create venv ok')
    runfile_copy(paths,runfile)
    print('runfile copy done!')
    set_Infoplist()
    print('info priset done')
    set_permissions(paths)
    print('done!')


