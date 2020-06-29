import sys


def main():
    path = sys.argv[1]
    print('hello boltpack!')
    import createapp
    createapp.main([path],path)
    print('main.py done')

