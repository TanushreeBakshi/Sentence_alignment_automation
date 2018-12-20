#CODE WRITTEN BY: Tanushree Bakshi (nagpur intern SVPCET) IT 2019 batch

#Make Directories
mkdir ArrowFiles_$1
mkdir AlignedFiles_$1
mkdir AdhyayE_$1/SentenceFiles
mkdir AdhyayH_$1/SentenceFiles
#================================
#Count number of files in directory
echo "count is $count"
cd AdhyayE_$1
for file in $(ls -l | grep .txt);
do
	if [ -f $file ]; then
		count=$(expr $count + 1)
	fi
done
cd ..
echo "count is $count"

#====================================
#Access English folder, read file "e$i", split "e$i" to "sen_e$i", feed to champollion $1
for i in `seq 1 $count`;
do
	bash split_english_para.sh ./AdhyayE_$1/e_$i.txt sen_e_$i

#====================================
#Access Hindi folder, read file "h$i", split "h$i" to "sen_h$i", feed to champollion $2

	bash split_hindi_para.sh ./AdhyayH_$1/h_$i.txt sen_h_$i

#================================
#Champollion output <=> file

	bash run_sentence_alignment.sh sen_e_$i sen_h_$i


#==============================
#Handle omitted sentences

	python omitted_lines.py a_sen_e_$i.txt sen_h_$i sen_e_$i abc.txt $i
	cat abc.txt >> omitted_lines.txt
	rm $i.txt

#===============================
#Roza mam code .c to align using <=> file create "align_$i" file

	./align-eng-hin.out a_sen_e_$i.txt sen_h_$i sen_e_$i aligned_$i.txt

#==============================
#Move unrequired files

	mv a_sen_e_$i.txt ArrowFiles_$1
	mv aligned_$i.txt AlignedFiles_$1
	mv sen_e_$i AdhyayE_$1/SentenceFiles
	mv sen_h_$i AdhyayH_$1/SentenceFiles

done

#=================================================
#Save omitted file in Omitted folder for traceback

	mv omitted_lines.txt Omitted
#===============================
#Combine all aligned files into "merge" file

cd AlignedFiles_$1
cat $(find ./ -name "aligned_*" | sort -V) > merge_$1
cd ..
