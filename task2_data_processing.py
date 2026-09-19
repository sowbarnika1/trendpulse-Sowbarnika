import datetime

import pandas as pd

df = pd.read_json('\\data\\trends_20260919.json')


df.drop_duplicates(subset=["post_id"])
print(f"After removing duplicates: {len(df)}")
df.dropna(subset=['post_id','title','score'])
print(f"After removing nulls: {len(df)}")
df['score']=df['score'].astype(int)
df['num_comments']=df['num_comments'].astype(int)
df = df.drop(df[df["score"] < 5].index)
print(f"After removing low scores: {len(df)}")
df['title']=df['title'].str.strip()

filename = "data/trends_clean.csv"

df.to_csv(filename,index=False)

print (f"Saved {len(df)} rows to data/trends_clean.csv")

print(f"Stories per category: {df["category"].value_counts()}")
