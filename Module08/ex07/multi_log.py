import numpy as np
import pandas
import math

if __name__ == "__main__":
	X = np.array(pandas.read_csv("../assets/solar_system_census.csv"))[:,1:]
	Y = np.array(pandas.read_csv("../assets/solar_system_census_planets.csv"))[:,1:]
