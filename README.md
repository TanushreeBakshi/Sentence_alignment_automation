=========================================================
# README
=========================================================

1. git clone Champollion Tool Kit V1.2 and add these files.

2. in Champollion Tool Kit V1.2 check
:preprocess folder - comp.sh file replace-stanford-punct.lex files [IMP],
:champollion-1.2 folder - [download from git]

3. open run_indiv_adhyay.sh file

4. change count of adhyays you have

5. save english adhyay as english_1...english_5 without .txt extension

6. save hindi adhyay as hindi_1...hindi_5 without .txt extension

7. pre-processing of data: 
	-find all ";" and replace with "@" in each input file
[this is because the tool introduces its own ";" while aligning and original ";" may be lost at the end]
	-make sure english_1... files and hindi_1... files DOES NOT contain any "\n and space" i.e an empty line with a space or tab

8. run code:
		bash run_indiv_adhyay.sh

==============================================
# run_indiv_adhyay.sh
----------------------------------------------

Uses codes:
1. run_sentence_alignment.sh
-for initial paragraph alignment

2. removes empty lines from original files

3. ./align-eng-hin.out
-for producing aligned files of paragraphs (check purpose)

4. div_eng_hin.py
-for creating paragraph files of individual adhyay and removing complete paragraphs that did not align into Omitted folder (backtrack)

5. rename_e.py and rename_h.py
-for renaming files into increasing order
(if a file number is not available the tool crashes)

6. split_para_and_feed.sh
-for running sentence alignment on paragraph files

================================================
# ./align-eng-hin.out  [IMPORTANT]
------------------------------------------------

run command:
	bash compile.sh
-to produce align-eng-hin.out file from align-eng-hin.c file and check the champollion installation

=================================================
# div_eng_hin.py
-------------------------------------------------

requires python
command: python div_eng_hin.py <champollion_output_file> <english_file> <hindi_file> <count_as_a_number(naming purpose[IMP])>

-dividing complete file into paragraphs as they are aligned by champollion
-moves omitted paragraphs into Omitted file along with their adhyay and paragraph number (backtracking)

=================================================
# split_para_and_feed.sh
-------------------------------------------------

uses codes:

1. split_english_para.sh :
	command: bash split_english_para.sh <paragraph_file_english> <sentences_ouput_file_english>
	example: bash split_english_para.sh ./AdhyayE_$1/e_$i.txt sen_e_$i

	-for accessing paragraph file inside english adhyay and creating corresponding sentence splitted files

2. split_hindi_para.sh :
	command: bash split_hindi_para.sh <paragraph_file_hindi> <sentences_ouput_file_hindi>
	example: bash split_hindi_para.sh ./AdhyayH_$1/h_$i.txt sen_h_$i

	-for accessing paragraph file inside english adhyay and creating corresponding sentence splitted files

3. run_sentence_alignment.sh :
	-produces alignment arrow files using champollion
	command: bash run_sentence_alignment.sh <english_sentence_file> <hindi_sentence_file>
	-output format:
1 <=> 1
2 <=> 2,3
3,4 <=> omitted
etc...

4. omitted_lines.py :
	-copies the sentences that are not aligned into a file "abc.txt" later appended every new file data into "omitted_lines.txt" file

5. ./align-eng-hin.out:
	-aligning the sentences next to each other
	-output format: english_sentence <=> hindi_sentence

6. finally every unrequired file in the main folder copied to another folder for readablity purpose.

7. Final adhyay sentences aligned merged into single file.

======================================================
# END TASK
-----------------------------------------------------

1. copy every merge file from each adhyay into your own folder and merge using command: 
	cat $(find ./ -name "merge_*" | sort -V) >  <aligned_file>

2. <aligned_file> is your final output file.

3. open the file and press ctrl+h :
	-find all "\n ; " and replace with " ; "
	-find all "@" and replace with ";"

[this is because the tool introduces its own ";" while aligning and original ";" may be lost at the end]

=========================================================

tool developed under internship project:
# "Automation of bilingual sentence alignment tool"
Tanushree Bakshi
Hrishikesh Ladikar
