#!/usr/bin/env python3
"""
Purpose: Tetranucleotide frequency
"""

import argparse
from typing import NamedTuple, Tuple


class Args(NamedTuple):
    """Command-line arguments"""
    dna: str

# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        'dna',
        metavar='DNA',
        help='Input DNA sequence',
    )

    args = parser.parse_args()

    with open(args.dna) as file:
            dna_sequence = file.read().strip()

    return Args(dna_sequence)

# --------------------------------------------------
def count_nucleotides(dna_sequence: str) -> Tuple[int, int, int, int]:
    """
    Count the frequency of each nucleotide in a DNA sequence.

    Args:
        dna_sequence (str): The DNA sequence to analyze.

    Returns:
        tuple[int, int, int, int]: Frequency of A, C, G, and T in the sequence.
    """

    count_a = dna_sequence.upper().count("A")
    count_c = dna_sequence.upper().count("C")
    count_g = dna_sequence.upper().count("G")
    count_t = dna_sequence.upper().count("T")

    return count_a, count_c, count_g, count_t 

# --------------------------------------------------
def main() -> None:
    """Main entry point"""

    args = get_args()
    result = count_nucleotides(args.dna_sequence)
    print(*result) 

# --------------------------------------------------
if __name__ == '__main__':
    main()
