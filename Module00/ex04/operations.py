import sys

if len(sys.argv) == 1:
	sys.exit("Usage: python operations.py <number1> <number2>", "Example:", "    python operations.py 10 3", sep="\n")
elif len(sys.argv) != 3:
	sys.exit("the number of arguments must be equal to 2")

try:
	n1 = int(sys.argv[1])
	n2 = int(sys.argv[2])
except:
	sys.exit("arguments must be integer")

print("Sum: {}".format(n1 + n2),
	"Difference: {}".format(n1 - n2),
	"Product: {}".format(n1 * n2),
	"Quotient: {}".format("ERROR (division by zero)" if n2 == 0 else n1 / n2), 
	"Remainder: {}".format("ERROR (modulo by zero)" if n2 == 0 else n1 % n2), sep='\n')