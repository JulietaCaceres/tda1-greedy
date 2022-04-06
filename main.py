from solucion_optima import *
import argparse

parser = argparse.ArgumentParser(description="Obtain the optimal solution")
parser.add_argument("k", help="Size of the road", default=500)
parser.add_argument("file", help="File with contracts", default="contratos.txt")


if __name__ == "__main__":
    args = parser.parse_args()
    print(best_contracts(int(args.k), args.file))








