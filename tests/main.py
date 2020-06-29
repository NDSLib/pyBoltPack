import testapp
testapp.__name__ = "__main__"


import subprocess

subprocess.run('python3 testapp.py'.split())
