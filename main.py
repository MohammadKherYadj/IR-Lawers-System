import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

class Preprocessing_EN:
  @staticmethod
  def process(sentance):
    sentance = Preprocessing_EN.remove_symbols(sentance)
    sentance = Preprocessing_EN.tokenizer(sentance)
    sentance = Preprocessing_EN.normalizer(sentance)
    sentance = Preprocessing_EN.remove_stopwords(sentance)
    sentance = Preprocessing_EN.remove_deplicate(sentance)
    return sentance

  @staticmethod
  def tokenizer(sentance):
    nltk.download("punkt")
    nltk.download("punkt_tab")
    words = word_tokenize(sentance)
    return words

  @staticmethod
  def normalizer(sentance):
    return [word.lower() for word in sentance]

  @staticmethod
  def remove_stopwords(sentance):
    nltk.download("stopwords")
    stop_words = set(stopwords.words('english'))

    sentance = [word for word in sentance if word not in stop_words]
    return sentance

  @staticmethod
  def lemmatization(sentance):
    pass

  @staticmethod
  def stemming(sentance):
    pass

  @staticmethod
  def remove_symbols(sentance):
    return re.sub(r'[^A-Za-z0-9\s]',' ',sentance)

  @staticmethod
  def remove_deplicate(sentance):
    return list(set(sentance))

