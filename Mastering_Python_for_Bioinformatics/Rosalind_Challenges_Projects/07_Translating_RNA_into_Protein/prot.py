#!/usr/bin/env python3
"""
Purpose: Translate RNA to proteins
"""

import argparse
from typing import NamedTuple, List

class Args(NamedTuple):
    """Command-line arguments"""
    rna_sequence: str

# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Translate RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('rna_sequence',
                        metavar='RNA',
                        type=str,
                        help='RNA sequence')

    args = parser.parse_args()
    return Args(rna_sequence=args.rna_sequence)

# --------------------------------------------------
def main() -> None:
    """Main entry point"""
    args = get_args()
    protein_sequence = translate_rna_to_protein(args.rna_sequence)
    print(protein_sequence)

# --------------------------------------------------
def translate_rna_to_protein(rna_sequence: str) -> str:
    """Translate RNA sequence into protein sequence
    
    Args:
        rna_sequence (str): The RNA sequence to be translated.
    
    Returns:
        str: The translated protein sequence.
    """
    # Genetic code dictionary with one-letter abbreviations
    genetic_code = {
        'UUU': 'F', 'UUC': 'F',  # Phenylalanine
        'UUA': 'L', 'UUG': 'L',  # Leucine
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',  # Leucine
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I',  # Isoleucine
        'AUG': 'M',  # Methionine (start)
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',  # Valine
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',  # Serine
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',  # Proline
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',  # Threonine
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',  # Alanine
        'UAU': 'Y', 'UAC': 'Y',  # Tyrosine
        'UAA': 'Stop', 'UAG': 'Stop',  # Stop codons
        'CAU': 'H', 'CAC': 'H',  # Histidine
        'CAA': 'Q', 'CAG': 'Q',  # Glutamine
        'AAU': 'N', 'AAC': 'N',  # Asparagine
        'AAA': 'K', 'AAG': 'K',  # Lysine
        'GAU': 'D', 'GAC': 'D',  # Aspartic acid
        'GAA': 'E', 'GAG': 'E',  # Glutamic acid
        'UGU': 'C', 'UGC': 'C',  # Cysteine
        'UGA': 'Stop',  # Stop codon
        'UGG': 'W',  # Tryptophan
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',  # Arginine
        'AGU': 'S', 'AGC': 'S',  # Serine
        'AGA': 'R', 'AGG': 'R',  # Arginine
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'  # Glycine
    }
    protein_list = []
    for codon in split_into_codons(rna_sequence):
        if codon in ['UGA', 'UAG', 'UAA']:
            break
        protein_list.append(genetic_code.get(codon))
    return "".join(protein_list)

# --------------------------------------------------
def split_into_codons(rna_sequence: str) -> List[str]:
    """Split RNA sequence into codons (triplets of nucleotides)"""
    return [rna_sequence[i:i+3] for i in range(0, len(rna_sequence) - len(rna_sequence) % 3, 3)]

# --------------------------------------------------
if __name__ == '__main__':
    main()
