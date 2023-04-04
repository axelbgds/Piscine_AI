from email import iterators

def ft_map(func, iterable):
	if not (isinstance(iterable, list) or isinstance(iterable, tuple) or isinstance(iterable, iterators)):
		return None
	for elem in iterable:
		yield func(elem)
