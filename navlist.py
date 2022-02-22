import json, sys, os

with open('C:\\Users\\matth\\Documents\\Programming Projects\\CMD Navigation\\locations.json') as json_data:
	locations = json.load(json_data)

for shortcut, location in locations.items():
	print(shortcut, location)