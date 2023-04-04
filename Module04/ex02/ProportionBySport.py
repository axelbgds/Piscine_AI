from FileLoader import FileLoader

def proportion_by_sport(dataset, year, sport, gender):
	df = dataset[dataset["Year"] == year].drop_duplicates("Name")
	genderSet = df[df["Sex"] == gender]
	sportSet = genderSet[genderSet["Sport"] == sport]
	return sportSet.shape[0] / genderSet.shape[0]

# xx = FileLoader()
# df = xx.load("../assets/athlete_events.csv")
# print(proportion_by_sport(df, 2004, "Tennis", "F"))