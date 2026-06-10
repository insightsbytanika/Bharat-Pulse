import pandas as pd
import re
from nltk.corpus import stopwords

df= pd.read_csv("data/raw_data.csv")

def clean_text(text):
    text=str(text).lower()
    text = re.sub(r"http\S+", '', text)
    text = re.sub(r"@\w+", '', text)
    text = re.sub(r"[^a-z\s]" , '', text)
    stop_word = set(stopwords.words('english'))
    text = ''.join([word for word in text.split() if word not in stop_words])
    return text

def clean_dataframe(df):
    df = df.dropna(subset=['title','description'])
    df["clean text"] = df["title"] + "" + df["description"]
    