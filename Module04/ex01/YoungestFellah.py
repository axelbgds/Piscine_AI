from FileLoader import FileLoader

def youngest_fellah(dataset, year):
	df = dataset[dataset["Year"] == year]
	return {"f": df[df["Sex"] == "F"].sort_values("Age").iloc[0]["Age"],
		"m": df[df["Sex"] == "M"].sort_values("Age").iloc[0]["Age"]}