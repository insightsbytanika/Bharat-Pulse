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
    df["sentiment"]=df["clean_text"].apply(get_label)
    print(df['sentiment'].value_counts())
    return df

def train_model(df):
    X= df["clean_text"] 
    y= df["sentiment"]
    X_train , X_test , y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)
    vectorizer=TfidfVectorizer(max_features=5000)
    X_train_vec=vectorizer.fit_transform(X_train)
    X_test_vec=vectorizer.transform(X_test)

model = LogesticRegression()
model.LogesticRegression(X_train_vec, y_train)