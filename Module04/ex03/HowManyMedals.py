from FileLoader import FileLoader

def proportion_by_sport(dataset, name):
	df = dataset[dataset["Name"] == name]
	res = dict()
	for year in df["Year"].unique():
		yearRes = df[df["Year"] == year]["Medal"].value_counts().to_dict()
		res[year] = {
			'G': yearRes['Gold'] if yearRes.get('Gold') else 0,
			'S': yearRes['Silver'] if yearRes.get('Silver') else 0,
			'B': yearRes['Bronze'] if yearRes.get('Bronze') else 0
		}
	return res

xx = FileLoader()
df = xx.load("../assets/athlete_events.csv")
print(proportion_by_sport(df, "Kjetil Andr Aamodt"))