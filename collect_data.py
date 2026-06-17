import requests 
import pandas as pd
import time
from config import API_KEY , QUERY , PAGES ,PAGE_SIZE , LANGUAGE
def fetch_articles():
    articles=[]
    print("starting data collection")

    for query in QUERY:
        print(f"fetching {query}")
        for page in range(1, PAGES + 1):
            print(f"fetching page {page} of {PAGES}")
            url = f"https://newsapi.org/v2/everything?q={QUERY}&language={LANGUAGE}&pageSize={PAGE_SIZE}&page={page}&apiKey={API_KEY}"
            response = requests.get(url)
            data=response.json()
            if data["status"]!= "ok":
                print(f"Error in page {page}: {data['message']}")
                break
            for article in data["articles"]:
                articles.append({
                    "title": article["title"],
                    "description": article["description"],
                    "published_At": article["publishedAt"]
                })
        time.sleep(1)
    print(f"total articles collected : {len(articles)}")
    return articles

def save_to_csv(articles):
    df=pd.DataFrame(articles)
    df.to_csv("data/raw_data.csv", index= False)
    print(f"Data saved to data/raw_data.csv - {len(df)} articles")

if __name__=="__main__":
    articles=fetch_articles()
    save_to_csv(articles)
