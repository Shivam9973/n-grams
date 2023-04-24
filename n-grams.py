# pip install -U textblob 
# pip install -r textblob.download_corpora

import nltk
nltk.download('punkt')

from textblob import TextBlob

sentence = "Technology is best when it brings people together"

ngram_object = TextBlob(sentence)

bigrams = ngram_object.ngrams(n=2) # Computing Bigrams
print("Bigrams: ", bigrams) 

trigrams = ngram_object.ngrams(n=3) # Computing Trigrams
print("Trigrams: ", trigrams) 