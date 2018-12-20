#CODE WRITTEN BY: Tanushree Bakshi (nagpur intern SVPCET) IT 2019 batch

#command: bash run_indiv_adhyay.sh

for i in `seq 1 18`;
do
	bash run_sentence_alignment.sh english_$i hindi_$i

echo "paragraphs aligned and arrow file produced"	

sed  '/^$/d' < english_$i > e
mv e english_$i

echo "english empty lines removed"

sed  '/^$/d' < hindi_$i > h
mv h hindi_$i

echo "hindi empty lines removed"
	
	./align-eng-hin.out a_english_$i.txt hindi_$i english_$i adhyay_aligned_$i.txt

echo "final para align file produced (BACKTRACKING)"
	
	python div_eng_hin.py a_english_$i.txt english_$i hindi_$i $i

echo "paragraphs splitted into files"

	cp rename_e.py AdhyayE_$i
	cd AdhyayE_$i
	python rename_e.py
	cd ..
echo "english files renamed"

	cp rename_h.py AdhyayH_$i
	cd AdhyayH_$i
	python rename_h.py
	cd ..

echo "hindi files renamed"s

	bash split_para_and_feed.sh $i

echo "done"
done
