import sys

if len(sys.argv) == 1:
	exit()
elif len(sys.argv) != 2:
	sys.exit("AssertionError: more than one argumnet are provided")

try :
	nb = int(sys.argv[1])
except:
	sys.exit("AssertionError: argument is not an integer")

print("I'm Zero." if nb == 0 else "I'm Even." if nb % 2 == 0 else "I'm Odd.")