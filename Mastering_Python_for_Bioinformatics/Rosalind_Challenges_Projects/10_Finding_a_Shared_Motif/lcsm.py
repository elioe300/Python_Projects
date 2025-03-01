#!/usr/bin/env python3
"""
Purpose: Longest Common Substring
"""

import argparse
from typing import NamedTuple, TextIO, Tuple, List
from Bio import SeqIO

class Args(NamedTuple):
    """Command-line arguments"""
    fasta_file: TextIO

# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Longest Common Substring',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('fasta_file',
                        metavar='FILE',
                        type=argparse.FileType("rt"),
                        help='Input FASTA file')
    args = parser.parse_args()

    return Args(fasta_file=args.fasta_file)

# --------------------------------------------------
def get_sequences_and_min_length(fasta_file: TextIO) -> Tuple[List[str], int]:
    """Get sequences and the minimum length
    
    Args:
        fasta_file (TextIO): The input FASTA file with sequences.
    
    Returns:
        Tuple[List[str], int]: List of sequences and the minimum length of the sequences.
    """
    sequences = [str(record.seq) for record in SeqIO.parse(fasta_file, "fasta")]
    min_length = min(map(len, sequences))
    return sequences, min_length

# --------------------------------------------------
def main() -> None:
    """Main entry point"""
    args = get_args()
    sequences, min_kmer_length = get_sequences_and_min_length(args.fasta_file)
    motif_dict = {}

    for sequence in sequences:
        for kmer_length in range(min_kmer_length, 1, -1):
            kmers = set([sequence[i:i + kmer_length] for i in range(0, len(sequence) - kmer_length + 1)])
            for kmer in kmers:
                motif_dict.setdefault(kmer, []).append(sequence)

    for kmer, sequences_containing_kmer in motif_dict.items():
        if len(sequences_containing_kmer) == len(sequences):
            print(kmer)
            break

# --------------------------------------------------
if __name__ == '__main__':
    main()
