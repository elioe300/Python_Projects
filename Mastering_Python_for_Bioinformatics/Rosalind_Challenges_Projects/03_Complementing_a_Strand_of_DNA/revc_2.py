#!/usr/bin/env python3
"""
Purpose: Print the reverse complement of a DNA sequence
"""

import argparse
from typing import NamedTuple
import os

class Args(NamedTuple):
    """Command-line arguments"""
    dna_sequence: str

# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print the reverse complement of DNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna_sequence',
                        metavar='DNA',
                        help='Input DNA sequence or file')

    args = parser.parse_args()

    # Check if the input is a file and read its content
    if os.path.isfile(args.dna_sequence):
        with open(args.dna_sequence, "r") as f:
            args.dna_sequence = f.read().rstrip()

    return Args(args.dna_sequence)

# --------------------------------------------------
def main() -> None:
    """Main entry point"""

    args = get_args()
    dna_revc = reverse_complement(args.dna_sequence)
    print(dna_revc)

# --------------------------------------------------
def reverse_complement(dna_sequence: str) -> str:
    """Return the reverse complement of the given DNA sequence
    
    Args:
        dna_sequence (str): The DNA sequence to be processed.
    
    Returns:
        str: The reverse complement of the DNA sequence.
    """

    translation_table = { 'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'a': 't', 'c': 'g', 'g': 'c', 't': 'a' }
    complementary_dna = reversed([translation_table.get(nucleotide) for nucleotide in dna_sequence])
    return "".join(complementary_dna)

# --------------------------------------------------
if __name__ == '__main__':
    main()
