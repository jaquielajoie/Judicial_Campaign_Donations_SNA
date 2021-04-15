import os
import sys
import argparse
import numpy as np
import pandas as pd


def set_cmd_args(args):
    if args.file:
        cmd_file = args.file
    else:
        cmd_file = None

    return cmd_file

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CSV location...')
    parser.add_argument("-f", "--file", type=str,
                    help="Path to input file.")

    args = parser.parse_args()
    cmd_file = set_cmd_args(args)

    FILE_PATH = os.path.abspath(f"{cmd_file}")

    df = pd.read_csv(FILE_PATH)
    print(df.head())
