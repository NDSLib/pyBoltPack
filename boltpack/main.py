import sys


def main():
    _,path,requirements,*arg = sys.argv
    print('hello boltpack!')
    import createapp
    createapp.main([path],path,requirements=requirements)
    print('main.py done')

