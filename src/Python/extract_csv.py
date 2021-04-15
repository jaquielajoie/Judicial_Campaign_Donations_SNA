import os
import sys
import argparse
import numpy as np
import pandas as pd
from tabulate import tabulate


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

    cols = ['cycle', 'transaction.type', 'amount', 'date', 'contributor.name', 'recipient.name', 'recipient.party', 'recipient.type', 'recipient.state', 'seat', 'election.type']

    df = pd.read_csv(FILE_PATH, names=cols)
    df_all = pd.read_csv(FILE_PATH)
    #print(tabulate(df[:25], headers='keys', tablefmt='psql'))
    print(df_all.columns.values.tolist())
    print(df_all.head())
    #print(df[:5]["contributor.name"])
