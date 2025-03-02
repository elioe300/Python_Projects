#!/usr/bin/env python3
"""
Purpose: Grep through FASTX files
"""

import argparse
import sys
import os
import re
from Bio import SeqIO
from typing import List, NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    pattern: str
    files: List[TextIO]
    input_format: str
    output_format: str
    outfile: TextIO
    case_insensitive: bool 


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Grep through FASTX files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('pattern', 
                        metavar='PATTERN',
                        type=str,
                        help='Search pattern')
    
    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'), 
                        help='Input file(s)')
    
    parser.add_argument('-f',
                        '--format',
                        help='Input file format',
                        metavar='str',
                        choices=['fasta', 'fastq'], 
                        default='')
    
    parser.add_argument('-O',
                        '--outfmt',
                        help='Output file format',
                        metavar='str',
                        choices=['fasta', 'fastq', 'fasta-2line'], 
                        default='')
    
    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        type=argparse.FileType('wt'), 
                        metavar='FILE',
                        default=sys.stdout)
    
    parser.add_argument('-i', 
                        '--case_insensitive',
                        help='Case-insensitive search',
                        action='store_true')

    args = parser.parse_args()

    return Args(pattern=args.pattern,
                files=args.file,
                input_format=args.format,
                output_format=args.outfmt,
                outfile=args.outfile,
                case_insensitive=args.case_insensitive)


# --------------------------------------------------
def main():
    """Main function to execute the program"""

    args = get_args()
    regex = re.compile(args.pattern, re.IGNORECASE if args.case_insensitive else 0) 
    for file_handle in args.files:
        input_format = args.input_format or guess_format(file_handle.name)
        if not input_format: 
            sys.exit(f'Please specify file format for "{file_handle.name}"')
        output_format = args.output_format or input_format
        searcher(regex, file_handle, input_format, output_format, args.outfile)


# --------------------------------------------------
def guess_format(filename: str) -> str:
    """ Guess format from file extension """

    extensions = {
        ".fa": "fasta",
        ".fna": "fasta",
        ".faa": "fasta",
        ".fq": "fastq",
        ".fastq": "fastq"
    }
    if extensions.get(os.path.splitext(filename)[1]):
        return extensions.get(os.path.splitext(filename)[1])


# --------------------------------------------------
def searcher(pattern: re.Pattern, file_handle: TextIO, input_format: str, output_format: str, output_file: TextIO) -> None:
    """ Search sequences matching the pattern and write to the output file """
    for record in SeqIO.parse(file_handle, f"{input_format}"):
        if bool(pattern.search(record.id)):
            SeqIO.write(record, output_file, output_format)


# --------------------------------------------------
if __name__ == '__main__':
    main()
