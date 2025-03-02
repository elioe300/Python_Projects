#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Compute GC content
"""

import argparse
import sys
from typing import NamedTuple, TextIO, Tuple
from Bio import SeqIO

class CommandLineArgs(NamedTuple):
    """Command-line arguments"""
    file: TextIO

# --------------------------------------------------
def get_args() -> CommandLineArgs:
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Compute GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='?',
                        default=sys.stdin,
                        help='Input sequence file')

    args = parser.parse_args()
    return CommandLineArgs(file=args.file)

# --------------------------------------------------
def main() -> None:
    """Main entry point"""
    args = get_args()
    gc_id, gc_content = max_gc(args.file)
    print(f'{gc_id}: {gc_content:.6f}%')

# --------------------------------------------------
def max_gc(fasta_file: TextIO) -> Tuple[str, float]:
    """Compute GC content of all records, return highest GC content and ID.
    
    Args:
        fasta_file (TextIO): The input FASTA file with DNA sequences.
    
    Returns:
        Tuple[str, float]: The ID of the sequence with the highest GC content and the GC content itself.
    """
    recs = SeqIO.parse(fasta_file, 'fasta')
    id_seq_gc = [(rec.id, gc_calculator(rec.seq)) for rec in recs]
    return max(id_seq_gc, key=lambda x: x[1])

# --------------------------------------------------
def gc_calculator(dna_sequence: str) -> float:
    """Calculate GC content and return as percentage
    
    Args:
        dna_sequence (str): The DNA sequence to calculate GC content for.
    
    Returns:
        float: The GC content as a percentage.
    """
    g = dna_sequence.count('G')
    c = dna_sequence.count('C')
    gc_content = (g + c) / len(dna_sequence) * 100
    return gc_content

# --------------------------------------------------
if __name__ == '__main__':
    main()
