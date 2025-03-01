#!/usr/bin/env python3
"""
Purpose: Print the reverse complement of a DNA sequence
"""

import argparse
from typing import NamedTuple
import os

class CommandLineArgs(NamedTuple):
    """Command-line arguments"""
    dna_sequence: str

# --------------------------------------------------
def get_args() -> CommandLineArgs:
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
        with open(args.dna_sequence, "r") as file:
            args.dna_sequence = file.read().rstrip()

    return CommandLineArgs(dna_sequence=args.dna_sequence)

# --------------------------------------------------
def main() -> None:
    """Main entry point"""

    args = get_args()
    reverse_complement_dna = reverse_complement(args.dna_sequence)
    print(reverse_complement_dna)

# --------------------------------------------------
def reverse_complement(dna_sequence: str) -> str:
    """Returns the reverse complement of the given DNA sequence
    
    Args:
        dna_sequence (str): The DNA sequence to be processed.
    
    Returns:
        str: The reverse complement of the DNA sequence.
    """
    
    translation_table = str.maketrans("atcgATCG", "tagcTAGC")
    complementary_dna = dna_sequence.translate(translation_table)
    return complementary_dna[::-1] 

# --------------------------------------------------
if __name__ == '__main__':
    main()
