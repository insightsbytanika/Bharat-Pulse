import pandas as pd
import random

cricket_posts = [
    "Kohli played a brilliant innings today amazing performance",
    "What a magnificent century by Rohit Sharma outstanding",
    "India won the match incredible performance by the team",
    "Bumrah is the best bowler in the world right now",
    "Terrible batting performance by India today disappointing",
    "India lost again very poor show by the batsmen",
    "Worst cricket match I have ever seen pathetic bowling",
    "Disgusting performance team needs to improve badly",
    "India will play Australia tomorrow at 2pm",
    "Toss happened India chose to bat first today",
    "Match starts in one hour at Mumbai stadium",
    "Rohit Sharma is the current Indian cricket captain",
    "Shubman Gill scored another fifty great talent",
    "Horrible decisions by the captain cost India the match",
    "Outstanding fielding and bowling by team India today",
    "Very poor show no coordination in the team at all",
    "Weather conditions are clear for the match today",
    "IPL auction will be held next month in Mumbai",
]

# 200 posts automatically banao
posts = []
for i in range(200):
    text = random.choice(cricket_posts)
    posts.append({"clean_text": text, "published_At": f"2024-0{random.randint(1,9)}-{random.randint(10,28)}"})

df = pd.DataFrame(posts)
df.to_csv("data/clean_data.csv", index=False)
print(f"Done! {len(df)} posts saved!")
print(df.head())