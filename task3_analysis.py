import pandas as pd
import numpy as np

df=pd.read_csv("data\\trends_clean.csv")
print("First 5 rows : ",df.head(5))

print(f"Loaded data: ",df.shape)

meanscore= df['score'].mean()

meannum_comments=df['num_comments'].mean()

print("Average score   :",meanscore)
print("Average comments   :",meannum_comments)

print("--- NumPy Stats ---")
score = np.array(df['score'])
print("Mean Score :", np.mean(score) )
print("Median Score :", np.median(score) )
print("Standard deviation Score :", np.std(score) )
print("Min Score :", score.min())
print("Max Score :", score.max ())

category = df['category'].value_counts().idxmax()
comments = df[df["num_comments"] == df["num_comments"].max()]
print("Most stories in:", category)

print(f"Most commented story: {comments['title'].to_string(index=False)}   —  {comments['num_comments'].to_string(index=False)} comments")

df['engagement']= df['num_comments']/df['score'] + 1

df['is_popular'] = df['score'] > meanscore

filename = "data/trends_analysed.csv"

df.to_csv(filename,index=False)

print("saved to ",filename)
