from FileLoader import FileLoader

def how_many_medals_by_country(dataset, country):
	df = dataset[dataset["Team"] == country]

# should get rid of duplicates for team sport
	team_sports = [
		'Basketball', 'Football', 'Tug-Of-War', 'Badminton', 'Handball', 
		'Water Polo', 'Hockey', 'Rowing', 'Volleyball', 'Synchronized Swimming', 
		'Baseball', 'Rugby', 'Lacrosse', 'Polo'
	]

	res = dict()
	for year in sorted(df["Year"].unique()):
		yearRes = df[df["Year"] == year and df["Sport"] not in team_sports]["Medal"].value_counts().to_dict()
		res[year] = {
			'G': yearRes['Gold'] if yearRes.get('Gold') else 0,
			'S': yearRes['Silver'] if yearRes.get('Silver') else 0,
			'B': yearRes['Bronze'] if yearRes.get('Bronze') else 0
		}
	return res

xx = FileLoader()
df = xx.load("../assets/athlete_events.csv")
print(how_many_medals_by_country(df, "United States"))