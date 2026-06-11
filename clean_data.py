import pandas as pd
import re
import nltk 
from nltk.corpus import stopwords

# df= pd.read_csv("data/raw_data.csv")

def clean_text(text):
    text=str(text).lower()
    text = re.sub(r"http\S+", '', text)
    text = re.sub(r"@\w+", '', text)
    text = re.sub(r"[^a-z\s]" , '', text)
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

def clean_dataframe(df):
    df = df.dropna(subset=['title','description'])
    df["clean_text"] = df["title"] + " " + df["description"]
    df["clean_text"] = df["clean_text"].apply(clean_text)
    df = df[["clean_text", "published_At"]]
    return df

def save_clean_data(df):
    df.to_csv(r"data/clean_data.csv", index=False)
    print(f"Clean data saved - {len(df)} articles remaining")

if __name__=="__main__":
    df= pd.read_csv("data/raw_data.csv")
    df= clean_dataframe(df)
    save_clean_data(df)
