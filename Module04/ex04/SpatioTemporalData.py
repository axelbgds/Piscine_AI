from FileLoader import FileLoader

class SpatioTemporalData:
	def __init__(self, dataset):
		self.dataset = dataset

	def where(self, date):
		return self.dataset[self.dataset["Year"] == date].drop_duplicates("City")["City"].to_list()

	def when(self, location):
		return self.dataset[self.dataset["City"] == location].drop_duplicates("Year")["Year"].to_list()

xx = FileLoader()
dataset = xx.load("../assets/athlete_events.csv")

yy = SpatioTemporalData(dataset)
yy.where(2016)

yy.when('Athina')