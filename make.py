""" Builds mindustry scripts
"""

import os
import argparse


def main():
    """ Entry point """
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    os.system(f'python -m minpiler --clip {args.file}')
    os.system(f'python -m minpiler {args.file}')


main()
