#!/usr/bin/python3
import subprocess
import sys

pythonV = sys.argv[0]
splt = pythonV.split('/')[:-1]
pythonV = '/'.join(splt)
cmd = f'{pythonV}/venv/bin/python3 {pythonV}/testapp.py'
subprocess.run(cmd.split())
