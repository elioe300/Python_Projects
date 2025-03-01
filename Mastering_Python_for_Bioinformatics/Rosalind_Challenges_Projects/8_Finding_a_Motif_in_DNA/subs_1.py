#!/usr/bin/env python3
"""
Purpose: Find subsequences in a sequence
"""

import argparse
from typing import NamedTuple, Set

class Args(NamedTuple):
    """Command-line arguments"""
    sequence: str
    subsequence: str

# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Find subsequences in a sequence',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='seq',
                        type=str,
                        help='Sequence')

    parser.add_argument('subsequence',
                        metavar='subseq',
                        type=str,
                        help='Sub-sequence')

    args = parser.parse_args()
    return Args(sequence=args.sequence, subsequence=args.subsequence)

# --------------------------------------------------
def main() -> None:
    """Main entry point"""
    args = get_args()
    motifs = find_subsequences(args.sequence, args.subsequence)
    print(motifs)

# --------------------------------------------------
def find_subsequences(sequence: str, subsequence: str) -> str:
    """Find subsequences and return positions
    
    Args:
        sequence (str): The main sequence to search within.
        subsequence (str): The sub-sequence to search for.
    
    Returns:
        str: A space-separated string of positions where the sub-sequence is found.
    """
    index = 0
    motifs: Set[int] = set()
    while subsequence in sequence[index:]:
        index = sequence.index(subsequence, index) + 1
        motifs.add(index)
    return " ".join(map(str, sorted(motifs)))

# --------------------------------------------------
if __name__ == '__main__':
    main()
