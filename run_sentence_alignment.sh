## Written by Roja
## To run champollion
## Pre-requisite:
##	Parallel Corpus (source and target lang. Ex: English and Hindi)
##RUN:
##	sh run_sentence_alignment.sh ENG HND 
##OUTPUT:	ENG_final_align.txt
##NOTE:	Inputs should be one sentence per line. (Both ENG and HND)


MYPATH=`pwd`
export CTK=$MYPATH/champollion-1.2

grep -v "^$" $1 > eng
grep -v "^$" $2 > hnd

$CTK/bin/champollion.EH eng hnd a_$1.txt

#$MYPATH/align-eng-hnd.out $1_align.txt hnd  eng  $1_final_align.txt
