import os, sys

class CsvReader():
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		if not os.path.exists(filename):
			sys.exit("File not found")
		self.fileObj = open(filename, "r")
		self.raw = []
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom

		self.getdata()

	def __enter__(self):
		return self

	def __exit__(self, type, value, traceback):
		if traceback:
			traceback.print_exception
		self.fileObj.close()
		return True

	def getdata(self):
		if len(self.raw):
			return self.raw[self.skip_top + (1 if self.header else 0) : len(self.raw) - self.skip_bottom]
		fileByLine = self.fileObj.read().split('\n')
		width = len(fileByLine[0].split(self.sep))
		for n in range(len(fileByLine)):
			line = fileByLine[n].split(self.sep)
			if len(line) != width:
				raise Exception("Wrong CSV File Format")
			self.raw.append(line)
		return self.raw[self.skip_top + (1 if self.header else 0) : len(fileByLine) - self.skip_bottom] if len(self.raw) \
			else None

	def getheader(self):
		if self.header is False:
			return None
		if not len(self.raw):
			self.getdata()
			return self.raw[0] if len(self.raw) else None
		return self.raw[0]

if __name__ == "__main__":
	with CsvReader('bad.csv') as file:
		if file == None:
			print("File is corrupted")
