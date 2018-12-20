#CODE WRITTEN BY: Tanushree Bakshi (nagpur intern SVPCET) IT 2019 batch

import os, sys
import re
from string import Template

i = sys.argv[5]
infile = sys.argv[1]
outputfile = open(sys.argv[4],"w+")

def line_access_multi(r,filen):
	sen_file = open(filen,'r')
	fi = sen_file.readlines()
	i=0
	for l in fi:
		for a in r:
			b = int(a)
			if i == b-1:
				write = str(filen)+": line: "+str(b)+": "+l
				outputfile.write(l)
		i+=1

def line_access(n,filen):
	sen_file = open(filen,'r')
	fi = sen_file.readlines()
	i=0
	for l in fi:
		if i == n-1:
			write = str(filen)+": line: "+str(n)+": "+l
			outputfile.write(write)
		if i == n: break
		i+=1

temp = Template("$i.txt")
tem = temp.safe_substitute({'i' : i})
t = Template("awk '{\
   if ($3 == \"omitted\") print \"e \" $1 ;\
   if ($1 == \"omitted\") print \"h \" $3 }'  $inf > $tem")

command = t.safe_substitute({"inf" : infile, "tem" : tem})

os.system(command)

f = open(tem,'r')
for line in f.readlines():
	if 'h' in line:
		h = sys.argv[2]
		if ',' in line[2]:
			r = re.split('\s[,.]|[,.]', line[2])	
			line_access_multi(r,h)
		else:
			count = int(line[2])
			line_access(count,h)
	if 'e' in line:
		e = sys.argv[3]
		if ',' in line[2]:
			r = re.split('\s[,.]|[,.]', line[2])		
			line_access_multi(r,h)
		else:
			count = int(line[2])
			line_access(count,e)

