import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')


sentance = "Hello world! how are you"
words = word_tokenize(sentance)
print(words)