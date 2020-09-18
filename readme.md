## USAGE

Here you will get instruction on how to obtain the Twitter corpus and get the train and test sets used for the experiments.

### Required
- CoNLL skeleton files in which the words are anonymized (one file for each conversation/thread, provided in ``conll_skeleton``)
- files with token differences to re-create the tokenization (one file per tweet, provided in ``diff``)
- text files containing the message of each tweet. The tweets can be found and downloaded via their Tweet ID (all IDs are listed in ``tweet_ids.txt``).

### Make CoNLL-format files

After downloading all the tweets via their Tweet IDs, the text of each tweet should be saved in an individual text file, with the Tweet ID as the name and the .txt extension (e.g. ``0123456789.txt``).

 Example tweet: ``This is just a test. Hi Twitter!``

The texts have to be tokenized on spaces (only spaces, not on punctuation etc.), with one token per line. A file should look like this:

 ```
 This
 is
 just
 a
 test.
 Hi
 Twitter!
 ```

If a tweet is no longer available, no file should be created (not even an empty one); the words from this tweet will stay anonymized.

**Note:** Some tweets contain unusual characters like zero-width spaces, which make the spacing invisible. At those spaces, words should separated just like at visible spaces.
Specifically, in the tweet with ID ``950216535125082112``, the tokenized version of ``*** I can'tJks ***`` should be

```
***
I
can't
Jks
****
```

As a final step, running ``python make_conll.py <PATH TO TWEET TEXT FILES>`` will create the CoNLL files in ``conll``.


### Split into train and test set

To split into training and test sets used in re-training e2e (Lee et al, 2018), run ``python split_test_train.py <PATH TO CONLL FILES>``, the file format will appear in ``train`` and ``test``


### The CoNLL format

The CoNLL format mostly follows the original CoNLL-2012 format with some additional annotations.

```
COLUMN	CONTENT
0 		Thread ID
1 		Thread number
2 		Token number in sentence
3 		Token
4 		POS tag
5 		Parse info
6 		[always *]
7 		[always -]
8 		[always -]
9 		Speaker/User handle
10		Named entity type
11		NP form
12		Coreference ID
13		Clause boundary
14		lowest-level NP boundary
15		highest-level NP boundary
16		grammatical role
17		genericity
18		[Tweet number in thread]_[sentence number in tweet]_[token number in sentence]
```
