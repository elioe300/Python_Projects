#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Find locations of N-glycosylation motif
"""

import argparse
import os
import sys
import subprocess
import re
import shutil
from typing import NamedTuple, TextIO
from Bio import SeqIO

class CommandLineArgs(NamedTuple):
    """ Command-line arguments """
    input_file: TextIO
    output_dir: str

# --------------------------------------------------
def get_args() -> CommandLineArgs:
    """Parse and return command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Find locations of N-glycosylation motif',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input_file',
                        metavar='FILE',
                        type=argparse.FileType("rt"),
                        help='Input text file of UniProt IDs')
    
    parser.add_argument('-d',
                        '--download_dir',
                        metavar='DIR',
                        default='fasta',
                        type=str,
                        help='Directory to download FASTA files')
    
    args = parser.parse_args()

    # Create the download directory if it does not exist
    if not os.path.isdir(args.download_dir):
        os.makedirs(args.download_dir)
    
    return CommandLineArgs(args.input_file, args.download_dir)

# --------------------------------------------------
def main():
    """ Main program execution """
    args = get_args()
    output_directory = args.output_dir

    # Download the FASTA files into the specified directory
    fetch_fasta_files(args.input_file.name, output_directory)
    
    # Compile regex pattern to find N-glycosylation motifs
    pattern = re.compile('(?=(N[^P][ST][^P]))')

    # Process each downloaded FASTA file
    for fasta_file in os.listdir(output_directory):
        file_path = os.path.join(output_directory, fasta_file)
        for record in SeqIO.parse(file_path, 'fasta'):
            # Search for N-glycosylation motifs
            if matches := [match.start() + 1 for match in pattern.finditer(str(record.seq))]:
                uniprot_id = record.id.split('|')[1]
                print(uniprot_id)
                print(*matches)

    # Remove the download directory and its contents
    shutil.rmtree(output_directory)

# --------------------------------------------------
def fetch_fasta_files(input_file_path: str, download_dir: str):
    """ Download FASTA files from UniProt """
    with open(input_file_path, 'r') as file:
        for line in file:
            uniprot_id = line.rstrip()
            fasta_file_path = os.path.join(download_dir, f"{uniprot_id}.fasta")
            if not os.path.isfile(fasta_file_path):
                try:
                    subprocess.run(['bash', './fetch_fasta.sh', uniprot_id, download_dir], check=True)
                except subprocess.CalledProcessError as error:
                    print(f'Error running fetch_fasta.sh: {error}', file=sys.stderr)

# --------------------------------------------------
if __name__ == '__main__':
    main()
