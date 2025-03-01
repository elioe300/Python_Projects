#!/usr/bin/env python3
"""
Purpose: Find subsequences in a sequence
"""

import argparse
from typing import NamedTuple, Set

class CommandLineArgs(NamedTuple):
    """Command-line arguments"""
    sequence: str
    subsequence: str

# --------------------------------------------------
def get_args() -> CommandLineArgs:
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
    return CommandLineArgs(sequence=args.sequence, subsequence=args.subsequence)

# --------------------------------------------------
def main() -> None:
    """Main entry point"""
    args = get_args()
    motifs = find_subsequences(args.sequence, args.subsequence)
    print(" ".join(map(str, motifs)))

# --------------------------------------------------
def find_subsequences(sequence: str, subsequence: str) -> str:
    """Find subsequences and return positions
    
    Args:
        sequence (str): The main sequence to search within.
        subsequence (str): The sub-sequence to search for.
    
    Returns:
        str: A space-separated string of positions where the sub-sequence is found.
    """
    pos = 0
    motifs: Set[int] = set()
    while True:
        index = sequence.find(subsequence, pos)
        if index == -1:
            break
        pos += 1
        motifs.add(index + 1)
    return "".join(map(str, sorted(motifs)))

# --------------------------------------------------
if __name__ == '__main__':
    main()
