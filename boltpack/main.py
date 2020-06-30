import sys
import argparse

from fileallsearch import fileallsearch

def main():
    #_,path,requirements,*arg = sys.argv
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--requirements", help="increase output verbosity")
    parser.add_argument("-rf", "--runfile", help="increase output verbosity")
    parser.add_argument("-rp", "--runpath", help="increase output verbosity")
    parser.add_argument("-rd", "--rundirectory", help="increase output verbosity")
    args = parser.parse_args()
    print(args)
    import createapp
    filepaths = []
    # rambda
    for path in fileallsearch(args.runpath):
        filepaths.append(path)
    createapp.main(
        runfile=args.runfile,
        rundirectory=args.rundirectory,
        requirements=args.requirements)
    print('main.py done')

