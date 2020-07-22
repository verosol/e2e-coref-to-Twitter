1. chosetesttrain from separete twitter docs create test and train sets, named as part of wb ontonotes genre wb/eng/00/name
You should indicate directories inside.

2. stats_for_paper has two files inside. 
You should launch shell file, indicating the separetor (blank space or tabulation usually) and name of the file inside.

3. taketheverbmentionsout takes a train folder of the ontonotes and another empty one with the same structure of folders (like wb/eng/00, etc )and excludes verbal mentions from the ontonotes putting them into the second "train2" folder.
You shall indicated dirs inside.
There are 2 files in nw/xinhua which have a token annotated with 3+ mentions not covered by this script, which will give error with e2e-coref "setup_train" scripts. They have to be corrected manually.

4. create_json_files_for_json2conll works with the output of the e2e-coref prediction mode, separetes the files into one document per one json file needed for json2conll.

5. json2conll creates conll file out of the folder with json per each twitter document and the gold version file
python json2conll. py  gold.conll /folder_with_conls/ name_of_the_output_file

6. remove1st2nd removes first-second person pronouns from the conll file (the format be conformed to the original twitter id in first column).
python remove1st2nd.py input_file
