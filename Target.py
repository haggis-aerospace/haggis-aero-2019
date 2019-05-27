# Eva Lott
# Dundee Haggis-Aero 2019
# Contains the target location

class Target:
	lon = 0
	lat = 0
	letter = 0
	img_filename = 0
	
	def __init__(self, lon, lat, letter, img_filename):
		self.lon = lon
		self.lat = lat
		self.letter = letter
		self.img_filename = img_filename
