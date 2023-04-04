from email import iterators

def ft_reduce(func, iterable):
	if not (isinstance(iterable, list) or isinstance(iterable, tuple) or isinstance(iterable, iterators)):
		return None
	res = iterable[0]
	for n in range(1, len(iterable)):
		res = func(res, iterable[n])
	return res