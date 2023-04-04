import string, sys

def getTextSum(s):
	
	res = dict.fromkeys(["upper", "lower", "punc", "space", "etc"], 0)
	for c in s:
		res["upper" if c.isupper() else
		"lower" if c.islower() else
		"punc" if c in string.punctuation else
		"space" if c.isspace() else
		"etc"] += 1
	return res


def text_analyzer(s):
	'''
	This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text.
	'''
	if not isinstance(s, str):
		sys.exit("AssertionError: argument is not a string")
	print("The text contains {} character(s):".format(len(s)))
	resAnalysis = getTextSum(s)
	print("- {} upper letter(s)".format(resAnalysis["upper"]))
	print("- {} lower letter(s)".format(resAnalysis["lower"]))
	print("- {} punctuation mark(s)".format(resAnalysis["punc"]))
	print("- {} space(s)".format(resAnalysis["space"]))

if __name__ == "__main__":
	if len(sys.argv) != 2:
		sys.exit("Error: only one argument is expected." if len(sys.argv) > 2 else "Error: an argument is expected.")
	text_analyzer(sys.argv[1])