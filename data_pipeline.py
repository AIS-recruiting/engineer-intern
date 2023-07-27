import argparse
import pandas_solution
import naive_solution

# mypy, flake8, isort
parser = argparse.ArgumentParser(description="Pipeline to sqlite database")
parser.add_argument(
    '--mode', '-m',
    help='set mode',
    default='pandas',
    type=str,
    choices=['pandas', 'naive'],
    )

args = parser.parse_args()

if __name__ == "__main__":
    if args.mode == 'pandas':
        pandas_solution.csv_to_sqlite()
    else:
        naive_solution.csv_to_sqlite()
