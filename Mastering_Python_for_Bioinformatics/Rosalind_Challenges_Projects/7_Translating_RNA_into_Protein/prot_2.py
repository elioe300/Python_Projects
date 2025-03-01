#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Translate RNA to proteins
"""

import argparse
from typing import NamedTuple
from Bio.Seq import Seq


class Args(NamedTuple):
    """ Command-line arguments """
    rna: str


# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Translate RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('rna',
                        metavar='RNA',
                        type=str,
                        help='RNA sequence')

    args = parser.parse_args()
    return Args(rna=args.rna)


# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""
    args = get_args()
    rna_seq = Seq(args.rna)
    protein_seq = rna_seq.translate(to_stop=True)
    print(str(protein_seq))


# --------------------------------------------------
if __name__ == '__main__':
    main()
