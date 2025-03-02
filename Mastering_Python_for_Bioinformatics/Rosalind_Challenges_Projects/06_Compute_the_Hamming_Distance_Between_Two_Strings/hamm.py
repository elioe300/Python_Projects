#!/usr/bin/env python3
"""
Purpose: Calculate Hamming distance
"""

import argparse
from typing import NamedTuple
from itertools import zip_longest

class Args(NamedTuple):
    """Command-line arguments"""
    sequence1: str
    sequence2: str

# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Calculate Hamming distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence1',
                        metavar='str',
                        type=str,
                        help='First DNA sequence')

    parser.add_argument('sequence2',
                        metavar='str',
                        type=str,
                        help='Second DNA sequence')

    args = parser.parse_args()

    return Args(sequence1=args.sequence1, sequence2=args.sequence2)

# --------------------------------------------------
def main():
    """Main entry point"""

    args = get_args()
    hamming_distance_value = calculate_hamming_distance(args.sequence1, args.sequence2)
    print(hamming_distance_value)

# --------------------------------------------------
def calculate_hamming_distance(sequence1: str, sequence2: str) -> int:
    """Calculate the Hamming distance between two DNA sequences
    
    Args:
        sequence1 (str): First DNA sequence.
        sequence2 (str): Second DNA sequence.
    
    Returns:
        int: The Hamming distance between the two sequences.
    """

    hamming_distance_value = 0
    for nucleotide_pair in zip_longest(sequence1, sequence2):
        if nucleotide_pair[0] != nucleotide_pair[1]:
            hamming_distance_value += 1
    return hamming_distance_value

# --------------------------------------------------
if __name__ == '__main__':
    main()
