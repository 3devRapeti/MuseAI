import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

pd.set_option('display.max_columns', None)

data = pd.read_csv("lyrics-emotion-detection\OriginalAnnotations.csv", header = 0)
# print(data.columns)
# print(data['genre'].unique())
# print(data.describe())
# print(data.head(5))

data = data.drop(columns=['Unnamed: 0'])
# print(data.columns)
# print(data.isnull().sum())

stop_words = set(stopwords.words('english'))

tokens = []
for i in range (0, 5):
    token = word_tokenize(data['lyrics'][i:i+1][i].lower())
    token = [word for word in token if word.isalpha()]
    token = [word for word in token if word not in stop_words]
    print(len(list(set(token))))