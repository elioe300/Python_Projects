#!/usr/bin/env python3
"""
Purpose: Calculate Fibonacci sequence
"""

import argparse
from typing import NamedTuple

class Args(NamedTuple):
    """Command-line arguments"""
    generations: int
    litter_size: int

# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Calculate Fibonacci sequence',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('generations',
                        metavar='generations',
                        help='Number of generations',
                        type=int)

    parser.add_argument('litter_size',
                        metavar='litter',
                        help='Size of litter per generation',
                        type=int)

    args = parser.parse_args()

    # Validate the input arguments
    if not 1 <= args.generations <= 40:
        parser.error(f'generations "{args.generations}" must be between 1 and 40')
    if not 1 <= args.litter_size <= 5:
        parser.error(f'litter "{args.litter_size}" must be between 1 and 5')

    return Args(generations=args.generations, litter_size=args.litter_size)

# --------------------------------------------------
def main() -> None:
    """Main entry point"""

    args = get_args()
    fibo_result = fibonacci_generator(args.generations, args.litter_size)
    print(fibo_result)

# --------------------------------------------------
def fibonacci_generator(generations: int, litter_size: int) -> int:
    """Calculate Fibonacci sequence based on number of generations and litter size.

    Args:
        generations (int): Number of generations.
        litter_size (int): Size of litter per generation.

    Returns:
        int: The Fibonacci sequence value for the given parameters.
    """
    fib = [0, 1]
    for _ in range(generations - 1):
        fib.append(fib[-2] * litter_size + fib[-1])
    return fib[-1]

# --------------------------------------------------
if __name__ == '__main__':
    main()
