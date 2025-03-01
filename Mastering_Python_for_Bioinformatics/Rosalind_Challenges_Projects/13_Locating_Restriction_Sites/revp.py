#!/usr/bin/env python3
"""
Purpose: Locating Restriction Sites
"""

import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from typing import NamedTuple, TextIO

class Args(NamedTuple):
    """Command-line arguments"""
    fasta_file: TextIO

# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Locating Restriction Sites',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('fasta_file',
                        metavar='FILE',
                        type=argparse.FileType("rt"),
                        help='Input FASTA file')

    args = parser.parse_args()
    return Args(fasta_file=args.fasta_file)

# --------------------------------------------------
def main():
    """Main entry point"""
    args = get_args()
    for record in SeqIO.parse(args.fasta_file, "fasta"):
        seq = str(record.seq)
        # Iterate over different lengths of k-mers
        for length in range(4, 13):
            # Generate a list of k-mers of the current length
            kmer_list = [seq[kmer:kmer + length] for kmer in range(0, len(seq) - length + 1)]
            # Iterate over each k-mer in the list
            for index, kmer in enumerate(kmer_list):
                # Translate the k-mer to its reverse complement
                reverse_complement = str(Seq(kmer).reverse_complement())
                if kmer == reverse_complement:
                    print(index + 1, len(kmer))

# --------------------------------------------------
if __name__ == '__main__':
    main()
