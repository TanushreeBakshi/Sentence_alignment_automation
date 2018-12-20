import os
import glob
import re

def stringSplitByNumbers(x):
    r = re.compile('(\d+)')
    l = r.split(x)
    return [int(y) if y.isdigit() else y for y in l]

files = glob.glob('h*')

sorted_files = sorted(files, key = stringSplitByNumbers)
i = 1

for file in sorted_files:
	new = "h_" + str(i) + ".txt"
	print(file + '\t' + new)
	i += 1
	os.rename(file, new)
