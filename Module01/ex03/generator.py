import random, sys

def fisher_yates_shuffle(lst):
	for i in range(len(lst) - 1, 0, -1):
		j = random.randint(0, i + 1)
		lst[i], lst[j] = lst[j], lst[i]
	return lst
 
def generator(text, sep=" ", option=None):
	if not (isinstance(text, str) and isinstance(sep, str) and option in ["shuffle", "ordered", "unique", None]):
		sys.exit("input error")
	lst = text.split(sep)
	if option == "shuffle":
		lst = fisher_yates_shuffle(lst)
	elif option == "ordered":
		lst = sorted(lst)
	elif option == "unique":
		lst = list(dict.fromkeys(lst))
	for n in range(len(lst)):
		yield lst[n]
	