#!/usr/bin/env python3
"""
Purpose: Infer mRNA from Protein
"""

import argparse
import os
from functools import reduce
from typing import NamedTuple, List

class Args(NamedTuple):
    """Command-line arguments"""
    protein_sequence: str
    modulo: int

# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Infer mRNA from Protein',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('protein_sequence',
                        metavar='protein',
                        type=str,
                        help='Input protein sequence or file')

    parser.add_argument('-m',
                        '--modulo',
                        metavar='int',
                        type=int,
                        default=1000000,
                        help='Modulo value')

    args = parser.parse_args()

    # Check if the input is a file and read its contents if it is
    if os.path.isfile(args.protein_sequence):
        with open(args.protein_sequence, 'r') as f:
            args.protein_sequence = f.read().rstrip()

    return Args(protein_sequence=args.protein_sequence, modulo=args.modulo)

# --------------------------------------------------
def main():
    """Main entry point"""
    args = get_args()
    infer_mrna(args.protein_sequence, args.modulo)

# --------------------------------------------------
def infer_mrna(protein_sequence: str, modulo: int) -> int:
    """Infer the number of possible mRNA sequences for a given protein sequence
    
    Args:
        protein_sequence (str): The protein sequence to analyze.
        modulo (int): The modulo value for the output.
    
    Returns:
        int: The number of possible mRNA sequences modulo the given value.
    """
    # Dictionary of amino acids (keys) and their corresponding codons (values)
    codon_to_aa = {
        'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N', 'ACA': 'T',
        'ACC': 'T', 'ACG': 'T', 'ACU': 'T', 'AGA': 'R', 'AGC': 'S',
        'AGG': 'R', 'AGU': 'S', 'AUA': 'I', 'AUC': 'I', 'AUG': 'M',
        'AUU': 'I', 'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAU': 'H',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P', 'CGA': 'R',
        'CGC': 'R', 'CGG': 'R', 'CGU': 'R', 'CUA': 'L', 'CUC': 'L',
        'CUG': 'L', 'CUU': 'L', 'GAA': 'E', 'GAC': 'D', 'GAG': 'E',
        'GAU': 'D', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G', 'GUA': 'V',
        'GUC': 'V', 'GUG': 'V', 'GUU': 'V', 'UAC': 'Y', 'UAU': 'Y',
        'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S', 'UGC': 'C',
        'UGG': 'W', 'UGU': 'C', 'UUA': 'L', 'UUC': 'F', 'UUG': 'L',
        'UUU': 'F', 'UAA': '*', 'UAG': '*', 'UGA': '*',
    }

    # Obtain the possible codon lengths for each amino acid in protein_sequence + '*'
    possible_lengths = [
        len([c for c, res in codon_to_aa.items() if res == aa])
        for aa in protein_sequence + '*'
    ]
    print(modprod(possible_lengths, modulo))

# --------------------------------------------------
def modprod(xs: List[int], modulo: int) -> int:
    """Return the product modulo a value"""
    return reduce(lambda x, y: mulmod(x, y, modulo), xs, 1)

# --------------------------------------------------
def mulmod(a: int, b: int, mod: int) -> int:
    """Multiplication with modulo"""
    
    def maybemod(x):
        ret = (x % mod) if mod > 1 and x > mod else x
        return ret or x

    res = 0
    a = maybemod(a)
    while b > 0:
        if b % 2 == 1:
            res = maybemod(res + a)
        a = maybemod(a * 2)
        b //= 2

    return res

# --------------------------------------------------
if __name__ == '__main__':
    main()
