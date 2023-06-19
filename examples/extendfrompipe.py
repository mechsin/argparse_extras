
import argparse
from argparse_extras.actions import ExtendFromPipe

if __name__ == "__main__":

    desc = 'Implements Action class that reads from STDIN'
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('required')
    parser.add_argument('--optional')
    parser.add_argument('--newline', action=ExtendFromPipe)
    parser.add_argument('--spaces', action=ExtendFromPipe, delimiter=' ')
    parser.add_argument('--tabs', action=ExtendFromPipe, delimiter='\t')
    parser.add_argument('--asints', action=ExtendFromPipe, type=int)
    parser.add_argument('--null', action=ExtendFromPipe, delimiter='\0')
    cli_args = parser.parse_args()

    print(cli_args.required)
    print(cli_args.optional)
    print(cli_args.newline)
    print(cli_args.spaces)
    print(cli_args.tabs)
    print(cli_args.asints)
    print(cli_args.null)
