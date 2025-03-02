#!/usr/bin/env python3
"""
Purpose: Transcribe DNA into RNA
"""

import argparse
from typing import NamedTuple, List, TextIO
import os


class Args(NamedTuple):
    """Command-line arguments"""
    file: List[TextIO]
    out_dir: str

# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Transcribe DNA into RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input DNA file(s)',
                        nargs='+',
                        type=argparse.FileType("rt"))

    parser.add_argument('-o',
                        '--out_dir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='out')

    args = parser.parse_args()

    if not os.path.isdir(args.out_dir):
        os.makedirs(args.out_dir)

    return Args(file=args.file, out_dir=args.out_dir)

# --------------------------------------------------
def main() -> None:
    """Main entry point"""

    args = get_args()

    num_files, num_seqs = 0, 0
    for fh in args.file:
        num_files += 1
        input_path = fh.name
        filename = os.path.basename(input_path)
        out_file_path = os.path.join(args.out_dir, filename)

        # Process each line in the input file
        with fh as f, open(out_file_path, 'w') as out_f:
            for line in f:
                mrna = translateDNAtoRNA(line.strip())
                out_f.write(mrna + '\n')
                num_seqs += 1

    file_s = '' if num_files == 1 else 's'
    seqs_s = '' if num_seqs == 1 else 's'
    print(f"Done, wrote {num_seqs} sequence{seqs_s} in {num_files} file{file_s} to directory \"{args.out_dir}\".")

# --------------------------------------------------
def translateDNAtoRNA(dna: str) -> str:
    """Translate DNA sequence into RNA sequence

    Args:
        dna (str): The DNA sequence to transcribe.

    Returns:
        str: The transcribed RNA sequence.
    """
    mrna = dna.replace("T", "U")
    return mrna

# --------------------------------------------------
if __name__ == '__main__':
    main()
