import pandas

class FileLoader:
	def __init__(self):
		pass

	def load(self, path):
		# for now i'm supposing that it is a csv file
		file = pandas.read_csv(path)
		df = pandas.DataFrame(file)
		print("Data dimension: {} x {}".format(df.shape[0], df.shape[1]))
		return df

	def display(self, df, n):
		print(df[:n] if n >= 0 else df[n:])