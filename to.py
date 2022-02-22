
import sys, os, json

args = sys.argv[1:]
dest = " ".join(args).upper()

with open('locations.json') as json_data:
    locations = json.load(json_data)

if not dest in locations.keys():
	os.system("echo Destination not found")
else:
	print(locations[dest])