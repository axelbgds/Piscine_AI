import math

class TinyStatistician:
	def __init__(self):
		pass

	def mean(self, dataset):
		return sum(elem for elem in dataset) / len(dataset) if len(dataset) else None

	def median(self, dataset):
		slen = len(dataset)
		setsorted = sorted(dataset)
		if slen == 0:
			return None
		return float(setsorted[slen // 2]) if slen % 2 == 1 \
			else sum(setsorted[slen // 2 - 1 : slen // 2 + 1]) / 2

	def quartile(self, dataset):
		slen = len(dataset)
		setsorted = sorted(dataset)
		if slen == 0: # Idk yet what i should do if the set is too small
			return None
		return [
			self.median(setsorted[:slen // 2 + 1 if slen % 2 == 1 else 0]),
			self.median(setsorted[slen // 2:])
		]

	def percentile(self, dataset, percentage):
		print(percentage * len(dataset) / 100)

	def var(self, dataset):
		smean = self.mean(dataset)
		return sum((elem - smean) ** 2 for elem in dataset) / len(dataset)

	def std(self, dataset):
		return math.sqrt(self.var(dataset))

a = [1, 42, 300, 10, 59]
xx = TinyStatistician()

xx.percentile(a, 10)