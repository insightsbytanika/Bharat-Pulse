import pandas as pd
import pickle 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
 
def load_data():
    df= pd.read_csv("data/clean_data.csv")
    print(f"Total no of articles loaded {len(df)}")
    return df

def label_sentiment(df):
    analyser=SentimentIntensityAnalyzer()
    def get_label(text):
        score=analyser.polarity_scores(text)["compound"]
        if score>0.05:
            return "Positive"
        elif score<-0.05:
            return "Negative"
        else:
            return "Neutral"
        df["sentiment"]=df["sentiment"].apply(get_label)