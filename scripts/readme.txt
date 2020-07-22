1. chosetesttrain from separete twitter docs create test and train sets, named as part of wb ontonotes genre wb/eng/00/name
You should indicate directories inside.

2. stats_for_paper has two files inside. 
You should launch shell file, indicating the separetor (blank space or tabulation usually) and name of the file inside.

3. taketheverbmentionsout takes a train folder of the ontonotes and another empty one with the same structure of folders (like wb/eng/00, etc )and excludes verbal mentions from the ontonotes putting them into the second "train2" folder.
You shall indicated dirs inside.
There are files which have a token annotated with 3+ mentions not covered by this script, which can give error with e2e-coref "setup_train" scripts. They have to be corrected manually.

bc/msnbc/00/msnbc_0002.9v_gold_conll
79)|77)|76)|28)

pt/nt/66/nt_6605.9v_gold_conll
11)|8)|2)|0)

pt/nt/41/nt_4105.9v_gold_conll
(2|(7|(15|(16

bn/voa/02/voa_0261.9v_gold_conll
4)|3)|2)|0)

bn/pri/00/pri_0035.9v_gold_conll
(9)|22)|20)|19)

bn/pri/00/pri_0037.9v_gold_conll
9)|6)|3)|1)

bn/pri/00/pri_0038.9v_gold_conll
25)|22)|21)|18)

bn/pri/00/pri_0066.9v_gold_conll
17)|12)|5)|3)

bn/pri/00/pri_0094.9v_gold_conll
28)|7)|5)|0)

bn/cnn/02/cnn_0284.9v_gold_conll
27)|21)|18)|4)

bn/nbc/00/nbc_0008.9v_gold_conll
18)|12)|8)|5)

nw/wsj/10/wsj_1017.9v_gold_conll
31)|17)|11)|9)

nw/wsj/06/wsj_0655.9v_gold_conll
(6)|18)|16)|4)

nw/wsj/12/wsj_1299.9v_gold_conll
13)|7)|4)|2)

nw/wsj/13/wsj_1331.9v_gold_conll
48)|22)|20)|7)

nw/wsj/13/wsj_1366.9v_gold_conll
(13)|44)|42)|27)|24)

nw/wsj/14/wsj_1436.9v_gold_conll
24)|22)|13)|6)

nw/wsj/14/wsj_1466.9v_gold_conll
8)|7)|3)|1)

nw/xinhua/00/chtb_0024.9v_gold_conll
(7)|8)|6)|0)

nw/xinhua/00/chtb_0052.9v_gold_conll
12)|10)|7)|0)


4. create_json_files_for_json2conll works with the output of the e2e-coref prediction mode, separetes the files into one document per one json file needed for json2conll.

5. json2conll creates conll file out of the folder with json per each twitter document and the gold version file
python json2conll. py  gold.conll /folder_with_conls/ name_of_the_output_file

6. remove1st2nd removes first-second person pronouns from the conll file (the format be conformed to the original twitter id in first column).
python remove1st2nd.py input_file
