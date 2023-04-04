from email import iterators

def ft_filter(func, iterable):
	if not (isinstance(iterable, list) or isinstance(iterable, tuple) or isinstance(iterable, iterators)):
		return None
	for elem in iterable:
		if func(elem):
			yield elem