
import pandas as pd
import streamlit as st
import numpy as np
from joblib import load
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
import re

# Clean numbers, punctuation
# lowercasing
# split
# stemmer
def text_transformation(df_col):
    lm = WordNetLemmatizer()
    corpus = []
    for item in df_col:
        new_item = re.sub('[^a-zA-Z]',' ',str(item))
        new_item = new_item.lower()
        new_item = new_item.split()
        new_item = [lm.lemmatize(word) for word in new_item if word not in set(stopwords.words('english'))]
        corpus.append(' '.join(str(x) for x in new_item))
    return corpus

def expression_check(prediction_input):
    st.markdown(prediction_input)
    if (prediction_input).any() == -1:
        print("👎🏻 Negative Sentiment.")
    elif (prediction_input).all() == 1:
        print("👍🏻 Positive Sentiment.")
    else:
        print("Invalid Statement.")

# function to take the input statement and perform the same transformations we did earlier
def sentiment_predictor(input):
    input = text_transformation(input)

    lr1 = load("svc1.pkl")
    tfidf1 = load("tfidf1.pkl")

    transformed_input=tfidf1.transform(input)
    prediction = lr1.predict(transformed_input)
    expression_check(prediction)

# Sayfa Ayarları
st.set_page_config(
    page_title="NlP - Sentiment Analysis",
    page_icon="",
    layout="centered",
    menu_items={
        "Get help": "mailto:nygulzehra@gmail.com",
        "About": "For More Information\n" + "https://github.com/nygulzehra"
    }
)

st.title("**:black[Review Sentiment Analysis Project]**")
st.image("pos-neg.png")
st.markdown("Let's try it! ")
text = st.text_input("Write your text here" )

    # Sonuç Ekranı
if st.button("Submit"):

    st.info("*result*")
    sentiment_predictor("["+ text+"]")
