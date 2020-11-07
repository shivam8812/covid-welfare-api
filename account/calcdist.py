import numpy as np 
import math

def calculatedistance(latitude1, longitude1, latitude2, longitude2):
	difflat = ((latitude2 - latitude1)*math.pi)/180
	difflong =((longitude2 - longitude1)*math.pi)/180
	a = (np.sin(difflat/2))**2 + (np.cos((latitude1*math.pi)/180)) * (np.cos((latitude2*math.pi)/180)) * (np.sin(difflong/2)**2)
	c = 2*math.atan2(np.sqrt(a), np.sqrt(1-a))
	radius_of_earth = 6371
	return radius_of_earth*c


