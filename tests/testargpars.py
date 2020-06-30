import argparse
parser = argparse.ArgumentParser()
#parser.add_argument("square", type=int,
#                    help="display a square of a given number")
parser.add_argument("-r", "--requirements", help="increase output verbosity")
parser.add_argument("-rf", "--runfile", help="increase output verbosity")
args = parser.parse_args()
print(args)
#if args.verbosity == 2:
