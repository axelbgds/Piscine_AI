import pandas
import sys
from Kmeans import KmeansClustering

def parse(args):
	if len(sys.argv) != 4:
		sys.exit("Error: required number of arguments: 3")
	args = [elem.split("=") for elem in sys.argv[1:]]
	if not all(len(elem) == 2 for elem in args):
		sys.exit("Error: Wrong type of arguments")
	kmeans = {elem[0]:elem[1] for elem in args}
	if set(kmeans.keys() - set(["filepath", "ncentroid", "max_iter"])):
		sys.exit("Error: Wrong type of arguments")

if __name__ == "__main__":
	parse(sys.argv)