from argparse import ArgumentParser, Namespace

parser = ArgumentParser(description="Just a test")

parser.add_argument("square",help="square a given number", type=int)
parser.add_argument(
                    '-v', '--verbose', 
                    help='provide a verbose desc',
                    action='store_true',
                    type=int,
                    choices=[0, 1, 2]
                        )

args: Namespace = parser.parse_args()

if args.verbose == 0:
    print("option 1 ")
elif args.verbose == 1:
    print("option 2 ")
elif args.verbose == 2:
    print("option 3 ")

print(args.square ** 2)