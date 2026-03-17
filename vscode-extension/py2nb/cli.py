import argparse
from .converter import py_to_nb_file


def main():
    parser = argparse.ArgumentParser(
        description="Convert an annotated .py file to a Jupyter notebook."
    )
    parser.add_argument("input", help="Input .py file")
    parser.add_argument("-o", "--output", default=None,
                        help="Output .ipynb file (default: same name as input)")
    args = parser.parse_args()

    out = py_to_nb_file(args.input, args.output)
    print(f"Written: {out}")


if __name__ == "__main__":
    main()
