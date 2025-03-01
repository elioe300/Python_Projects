#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Compute GC content
"""

import argparse
from typing import NamedTuple


class Args(NamedTuple):
    """ Command-line arguments """
    rna: str


# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Translate RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('rna',
                        metavar='RNA',
                        type=str,
                        help='RNA sequence')

    args = parser.parse_args()
    return Args(rna=args.rna)


# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""
    args = get_args()
    codigo_genetico = {
        'UUU': 'F', 'UUC': 'F',  # Fenilalanina
        'UUA': 'L', 'UUG': 'L',  # Leucina
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',  # Leucina
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I',  # Isoleucina
        'AUG': 'M',  # Metionina (inicio)
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',  # Valina
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',  # Serina
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',  # Prolina
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',  # Treonina
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',  # Alanina
        'UAU': 'Y', 'UAC': 'Y',  # Tirosina
        'UAA': 'Stop', 'UAG': 'Stop',  # Codones de terminación
        'CAU': 'H', 'CAC': 'H',  # Histidina
        'CAA': 'Q', 'CAG': 'Q',  # Glutamina
        'AAU': 'N', 'AAC': 'N',  # Asparagina
        'AAA': 'K', 'AAG': 'K',  # Lisina
        'GAU': 'D', 'GAC': 'D',  # Ácido aspártico
        'GAA': 'E', 'GAG': 'E',  # Ácido glutámico
        'UGU': 'C', 'UGC': 'C',  # Cisteína
        'UGA': 'Stop',  # Codón de terminación
        'UGG': 'W',  # Triptófano
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',  # Arginina
        'AGU': 'S', 'AGC': 'S',  # Serina
        'AGA': 'R', 'AGG': 'R',  # Arginina
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'  # Glicina
    }
    list = []
    for i in range(0, len(args.rna) - len(args.rna) % 3,3):
        codon = args.rna[i:i+3]
        if codon in ['UGA', 'UAG', 'UAA']:
            break
        else:
            list.append(codigo_genetico.get(codon, "-"))
    print("".join(list))


# --------------------------------------------------
if __name__ == '__main__':
    main()
