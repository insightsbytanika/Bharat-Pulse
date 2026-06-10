import pandas as pd
import re
from nltk.corpus import stopwords

df= pd.read_csv("data/raw_data.csv")

def clean_text(text):
    text=str(text).lower()
