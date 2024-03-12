import string
import re
import numpy as np
import nltk
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import joblib
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack

import warnings

# Suppress all warnings
warnings.filterwarnings("ignore")


vectorizer = joblib.load("tfidfvectorizer.pkl")
log_reg_model = joblib.load("logistic_reg.pkl")


def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    ## remove numbers from the text
    text = re.sub(r"\d+", "", text)

    # Tokenize
    tokens = word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.lower() not in stop_words]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    ## remove single character words
    tokens = [word for word in tokens if len(word) > 1]

    # Join tokens back into strings
    text = ' '.join(tokens)
    text = [text]
    return text



def score(text:str,
          model,
          threshold:float) -> bool:
    
    no_of_words = len(text)
    ## vectorize the text
    text_vect = vectorizer.transform(preprocess_text(text))
    text_processed = hstack([text_vect, no_of_words])
    propensity = model.predict_proba(text_processed)

    if propensity[0][1] >= threshold: 
        prediction = 1
        propen = propensity[0][1]
    else: 
        prediction = 0
        propen = propensity[0][0]
    return prediction, propen