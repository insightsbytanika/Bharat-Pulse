import pandas as pd
import pickle 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
 
def load_data():
    df= pd.read_csv("data/clean_data.csv")
    print(f"Total no or articles loaded {len(df)}")
    return df

