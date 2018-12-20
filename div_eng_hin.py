#CODE WRITTEN BY: Tanushree Bakshi (nagpur intern SVPCET) IT 2019 batch

#command: python div_eng_hin.py <champollion_output_file> <english_file> <hindi_file> <count_as_a_number(naming purpose[IMP])>

import os, sys
import re
from string import Template

os.system("mkdir Omitted")
count = sys.argv[4]
print count

#=========line_access=============
def line_access(n,filen,f):
	eng_hinfile = open(filen,'r')
	fi = eng_hinfile.readlines()
	i=0
	eng = open(f,'w')
	for l in fi:
		if i == n-1:
			eng.write(l)
		if i == n: break
		i+=1


def line_access_multi(n,filen,f):
	eng_hinfile = open(filen,'r')
	fi = eng_hinfile.readlines()
	eng = open(f,'w')
	i=0
	for l in fi:
		for a in n:
			b = int(a)
			if i == b-1:
				eng.write(l)
		i+=1

#==========OmitDelete==========

with open(sys.argv[1]) as oldfile, open('no_omitted_'+count, 'w') as newfile, open('only_omitted_'+count,'w') as one:
	for line in oldfile:
		if not "omitted" in line:
			newfile.write(line)
		else:
			one.write(line)

#==========English========
os.system("awk '{print $1}' no_omitted_"+count+" > temp1")
n1 = open("temp1","r")
n = n1.readlines()
os.system("mkdir AdhyayE_"+count)
t = Template('./AdhyayE_$count/e$num.txt')
for num in n:
	num.replace(" ", "")
	if "," in num:
		r = re.split('\s[,.]|[,.]', num)
		num = r[0]
		f = t.substitute({'num' : num,'count' : count})
		line_access_multi(r,sys.argv[2],f)
	else:
		n = int(num)
		f = t.substitute({'num' : n,'count' : count})	
		line_access(n,sys.argv[2],f)

#========Hindi========

os.system("awk '{print $3}' no_omitted_"+count+" > temp2")
m1 = open("temp2","r")
m = m1.readlines()
os.system("mkdir AdhyayH_"+count)
y = Template('./AdhyayH_$count/h$num.txt')
for num in m:
	if "," in num:
		r = re.split('\s[,.]|[,.]', num)
		num = r[0]
		f = y.substitute({'num' : num,'count' : count})
		line_access_multi(r,sys.argv[3],f)
	else:
		n = int(num)
		f = y.substitute({'num' : n,'count' : count})	
		line_access(n,sys.argv[3],f)

#==========EnglishOmitted========
os.system("awk '{print $1}' only_omitted_"+count+" > temp3")
o1 = open("temp3","r")
o = o1.readlines()
w = Template('./Omitted/e_$c.$num.txt')
for num in o:
	if "omitted" in num:
		continue
	if "," in num:
		r = re.split('\s[,.]|[,.]', num)
		num = r[0]
		f = w.substitute(c = count,num = num)
		line_access_multi(r,sys.argv[2],f)
	else:
		n = int(num)
		f = w.substitute(c = count,num = n)
		line_access(n,sys.argv[2],f)

#========HindiOmitted========

os.system("awk '{print $3}' only_omitted_"+count+" > temp4")
p1 = open("temp4","r")
p = p1.readlines()
s = Template('./Omitted/h_$c.$num.txt')
for num in p:
	if "omitted" in num:
		continue
	if "," in num:
		r = re.split('\s[,.]|[,.]', num)
		num = r[0]
		f = s.substitute(c = count, num = num)
		line_access_multi(r,sys.argv[3],f)
	else:
		n = int(num)
		f = s.substitute(c = count, num = n)
		line_access(n,sys.argv[3],f)

os.system("rm temp1")
os.system("rm temp2")
os.system("rm temp3")
os.system("rm temp4")
