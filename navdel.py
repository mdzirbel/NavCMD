import json, sys, os

with open('C:\\Users\\matth\\Documents\\Programming Projects\\CMD Navigation\\locations.json') as json_data:
	locations = json.load(json_data)

args = sys.argv[1:]

dest = os.getcwd()

for arg in args:
	arg = arg.upper()
	if arg in locations.keys():
		print("deleting", arg)
		locations.pop(arg)
	else:
		locations[arg] = dest
		print(arg, "does not exist")

with open("C:\\Users\\matth\\Documents\\Programming Projects\\CMD Navigation\\locations.json", 'w') as f:
	json.dump(locations, f)

print("You can type 'navlist' to see the shortcut page")