import matplotlib.pyplot as plt
import pandas

from FileLoader import FileLoader

class MyPlotLib:
	def __init__(self):
		pass

	def histogram(self, data, features):
		set1 = data["Height"]
		set1 = set1.fillna(set1.median())
		print(set1)
		plt.hist(set1, bins=[125, 150, 175, 200, 225])

	def density(self, dataset, features):
		pass

	def pair_plot(self, dataset, features):
		pass

	def box_plot(self, dataset, features):
		pass

xx = FileLoader()
df = xx.load("../assets/athlete_events.csv")

tt = MyPlotLib()
tt.histogram(df, ["Weight", "Height"])