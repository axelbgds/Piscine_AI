import os, time

username = os.getenv('USER')

def logger(func):
	func_name = " ".join([word.capitalize() for word in func.__name__.split("_")])
	def wrapper(*args, **kwargs):
		fd = open("logger.log", "a")
		start = time.time()
		func(*args, **kwargs)
		execTime = str(round((time.time() - start) * 1000), 3) + "ms"
		fd.write(f"({username})Running: {func_name:20s}[ exec-time = {execTime}]\n")
		return func(*args, **kwargs)
	return wrapper