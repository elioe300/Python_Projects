#!/usr/bin/env python3
"""
Purpose: Mimic seqmagick
"""

import argparse
import os
from typing import NamedTuple, TextIO, List
from tabulate import tabulate
from Bio import SeqIO


class Arguments(NamedTuple):
    """Command-line arguments"""
    files: List[TextIO]
    table_format: str


# --------------------------------------------------
def get_args() -> Arguments:
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Mimic seqmagick',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='Input FASTA file(s)')

    parser.add_argument('-t',
                        '--table_format',
                        metavar='table',
                        type=str,
                        choices=[
                            'plain', 'simple', 'grid', 'pipe', 'orgtbl', 'rst',
                            'mediawiki', 'latex', 'latex_raw', 'latex_booktabs'
                        ],
                        default='plain',
                        help='Tabulate table style')

    args = parser.parse_args()

    return Arguments(args.files, args.table_format)


# --------------------------------------------------
def main():
    """Main function"""
    args = get_args()
    sequence_data = {}
    # Process files and store sequences in the dictionary
    for file_handle in args.files:
        file_name = file_handle.name
        sequence_data[file_name] = []
        for record in SeqIO.parse(file_name, "fasta"):
            sequence_data[file_name].append(str(record.seq))

    # Create a list of rows for the table
    table_rows = []
    for file_name, sequences in sequence_data.items():
        if len(sequences) == 0:
            total_length = 0
            min_length = 0
            max_length = 0
            avg_length = 0
            sequence_count = 0
        else:
            total_length = 0
            lengths = list(map(len, sequences))
            min_length = min(lengths)
            max_length = max(lengths)
            for sequence_count, sequence in enumerate(sequences, start=1):
                total_length += len(sequence)
            avg_length = total_length / sequence_count
        name = os.path.basename(file_name)
        table_rows.append([name, min_length, max_length, float(avg_length), sequence_count])

    # Define table headers
    headers = ["name", "min_len", "max_len", "avg_len", "num_seqs"]

    # Generate and display the table
    print(tabulate(table_rows, headers=headers, tablefmt=args.table_format, floatfmt='.2f'))


# --------------------------------------------------
if __name__ == '__main__':
    main()
