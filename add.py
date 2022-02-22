import json, sys, os

with open('C:\\Users\\matth\\Documents\\Programming Projects\\CMD Navigation\\locations.json') as json_data:
	locations = json.load(json_data)

args = sys.argv[1:]

dest = os.getcwd()

if len(args) == 0:
	os.system("navhelp")

for arg in args:
	arg = arg.upper()
	if arg in locations.keys():
		print(arg, "already exists and points to", locations[arg])
	else:
		locations[arg] = dest
		print("adding",arg)

with open("C:\\Users\\matth\\Documents\\Programming Projects\\CMD Navigation\\locations.json", 'w') as f:
	json.dump(locations, f)