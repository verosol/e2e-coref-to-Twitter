## The Corpus

This is an instruction on how to reproduce the Twitter Conversation Corpus used in *Adapting Coreference Resolution to Twitter Conversations*, which conforms with the Ontonotes annotation style except for the annotation of verb mention, which are annotated in Ontonotes but not this corpus. To conform with Twitter's Developer Policy, we only share our annotations as text files without including the full tweet contents and authors. Instead we provide the tweet IDs and also share an additional script and data to map our tokenization and annotations to the original tweets.

=======
### Required Data
- CoNLL skeleton files in which the words and tweet authors are anonymized (one file for each conversation/thread, provided in ``conll_skeleton``)
- files with token differences to re-create the tokenization (one file per tweet, provided in ``diff``)
- text files containing the message of each tweet. The tweets can be downloaded via their tweet ID through the Twitter API (all IDs are listed in ``tweet_ids.txt``).
- text files containing the author of each tweet (this is just one word per file, the username). The author can also be downloaded via the tweet ID.

### Make CoNLL-format files

After downloading all the tweets and authors via their Tweet IDs, the text of each tweet should be saved in an individual text file, with the tweet ID as the name and the .txt extension (e.g. ``0123456789.txt``). In a different directory, the authors should be stored in the same way, using the same file name (in this case ``0123456789.txt`` as well).

 Example tweet: ``This is just a test. Hi Twitter!``

The text then has to be tokenized on spaces (only spaces, not on punctuation etc.), with one token per line. A file should look like this:

 ```
 This
 is
 just
 a
 test.
 Hi
 Twitter!
 ```

If a tweet is no longer available, no files should be created (not even empty ones); the words and author will stay anonymized for this tweet.

**Note:** Some tweets may contain unusual characters like zero-width spaces, which make the spacing invisible. At those spaces, words should separated just like at visible spaces.
Specifically, in the tweet with ID ``950216535125082112``, the tokenized version of ``*** I can'tJks ***`` should be

```
***
I
can't
Jks
****
```

As a final step, running ``python make_conll.py <PATH TO TWEET TEXT FILES> <PATH TO AUTHOR FILES>`` will create the CoNLL files in ``conll``.


### Split into train and test set

<<<<<<< HEAD
To split into training and test sets used in re-training e2e (Lee et al, 2018), run ``python split_test_train.py <PATH TO CONLL FILES>``, the file format will appear in ``train`` and ``test``
=======
TODO: To split into training and test sets used in re-training e2e (Lee et al, 2018), run ``python split_test_train.py <PATH TO CONLL FILES>``, the file format will appear in ``train`` and ``test``

### Remove Verb mentions from Twitter Corpus and Ontonotes

TODO: how to use the script + manual corrections
>>>>>>> 3ca73beda320a26c59c57a8946586583ca5b12b5

### The CoNLL format

The CoNLL format for the corpus is inspired by the original CoNLL-2012 format with some differences.
Empty lines indicate sentence breaks.

```
COLUMN	CONTENT
0 		Thread ID
1 		Thread number
2 		Token number in sentence
3 		Token
4 		POS tag
5 		Parse info
6 		[always -]
7 		[always -]
8 		[always -]
9 		Speaker/User handle
10		Named entity type
12		Coreference ID
```
