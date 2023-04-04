import sys

if len(sys.argv) > 1:
	print((" ".join([s for s in sys.argv[1:] if len(s)])[::-1].swapcase()))