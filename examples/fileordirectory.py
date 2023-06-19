#!/usr/bin/env python

# Christopher Nyland
# 2022-07-13

# Code snippet that shows how to allow an argparse argument input to
# be either a path to a single file or a directory and either way
# return a list of the file paths.

import argparse
import os

from argparse_extras.types import FileOrDirectory

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="File or Directory example")

    kwargs = {
              'help': 'Takes file path or directory',
              'type': FileOrDirectory,
             }
    parser.add_argument('input', **kwargs)

    cli_args = parser.parse_args()

    print(cli_args.input)
