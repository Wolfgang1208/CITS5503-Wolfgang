import json
import sys, getopt
options, args = getopt.getopt(sys.argv[1:], 'hp:f:', ['filename='])

filename = ""

for name, value in options:
        if name in ('-f', '--filename'):
            filename = value
            print(filename)

with open(filename) as file_object:
    data = json.load(file_object)
print(data)