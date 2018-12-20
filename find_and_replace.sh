#python command: string.replace(s, old, new[, maxreplace])

#Bash command: sed -i 's/original/new/g' file.txt
#-i : in place of
#s: substitute
#original: original string or expression
#new: in place of word or expression
#g: global
#file.txt: file name

#IMPORTANT
# preprocessing of data

sed -i 's/\*/ /g' $1
sed -i 's/  */ /g' $1
sed -i 's/^ //g' $1
sed -i 's/;/@/g' $1
sed -i 's/?’/’?/g' $1
sed -i 's/\.’/’\./g' $1
sed -i 's/!’/’!/g' $1
