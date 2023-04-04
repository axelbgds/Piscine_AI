import sys, string

if len(sys.argv) != 3:
	sys.exit("Error: Wrong number of argument")
elif sys.argv[2].isdigit() == False:
	sys.exit("Error: Wrong type of argument")

print(list(filter(lambda x: len(x) > int(sys.argv[2]),
	[''.join([c for c in word if c not in string.punctuation]) for word in sys.argv[1].split(' ')])))