#!/usr/bin/env python3
"""
Purpose: Graph through sequences
"""

import argparse
import logging
from typing import NamedTuple, TextIO
from itertools import product
from pprint import pformat
from Bio import SeqIO

class Args(NamedTuple):
    """Command-line arguments"""
    fasta_file: TextIO
    overlap_size: int
    debug: bool

# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Graph through sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('fasta_file',
                        metavar='FILE',
                        type=argparse.FileType("rt"),
                        help='FASTA file')

    parser.add_argument('-k',
                        '--overlap_size',
                        metavar='size',
                        type=int,
                        default=3,
                        help='Size of overlap')

    parser.add_argument('-d',
                        '--debug',
                        action='store_true',
                        help='Enable debug mode')

    args = parser.parse_args()

    if args.overlap_size < 1:
        parser.error(f'--overlap_size "{args.overlap_size}" must be > 0')

    return Args(fasta_file=args.fasta_file, overlap_size=args.overlap_size, debug=args.debug)

# --------------------------------------------------
def main() -> None:
    """Main entry point"""
    args = get_args()
    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL)

    graph_sequences(args.fasta_file, args.overlap_size)

# --------------------------------------------------
def graph_sequences(fasta_file: TextIO, overlap_size: int) -> None:
    """Compute overlaps and create graphs through sequences
    
    Args:
        fasta_file (TextIO): The input FASTA file with sequences.
        overlap_size (int): The size of the overlap.
    """
    start_kmers, end_kmers = {}, {}
    for record in SeqIO.parse(fasta_file, "fasta"):
        kmers = [str(record.seq[i:i+overlap_size]) for i in range(0, len(record.seq) - overlap_size + 1)]
        start_kmers.setdefault(kmers[0], []).append(record.id)
        end_kmers.setdefault(kmers[-1], []).append(record.id)

    edges = []
    for kmer in set(start_kmers.keys()).intersection(end_kmers.keys()):
        pairs = product(start_kmers[kmer], end_kmers[kmer])
        filtered_pairs = filter(lambda p: p[0] != p[1], pairs)
        filtered_list = list(filtered_pairs)
        if filtered_list:
            edges.append(filtered_list)

    for edge_list in edges:
        for edge in edge_list:
            print(*edge)

    logging.debug('START_KMERS\n{}'.format(pformat(start_kmers)))
    logging.debug('END_KMERS\n{}'.format(pformat(end_kmers)))

# --------------------------------------------------
if __name__ == '__main__':
    main()
