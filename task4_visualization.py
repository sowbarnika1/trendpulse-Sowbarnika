import os

import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("output", exist_ok=True)

df=pd.read_csv("\\data\\trends_analysed.csv")
print(df.head)
plt.plot(df['score'])
plt.savefig("output/score_chart.png")
plt.show()

top10 = df.nlargest(10, "score").copy()
top10["short_title"] = top10["title"].apply(
    lambda x: x[:50] + x[:50] if len(x) > 50 else x
)

plt.figure(figsize=(10, 6))

plt.barh(
    top10["short_title"],
    top10["score"]
)

plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")

plt.gca().invert_yaxis()

plt.savefig("output/chart1_top_stories.png", bbox_inches="tight")
plt.show() 

category_counts = df["category"].value_counts()

plt.figure(figsize=(8, 5))

plt.bar(
    category_counts.index,
    category_counts.values,
    color=plt.cm.tab10(range(len(category_counts)))
)

plt.title("Number of Stories by Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")

plt.savefig(
    "output/chart2_categories.png",
    bbox_inches="tight"
)

plt.show()

popular=df[df['is_popular']==True]
non_popular=df[df['is_popular']==False]

plt.figure(figsize=(10,6))

plt.scatter(
    non_popular["score"],
    non_popular["num_comments"],
    color="blue",
    label="non-popular"

)

plt.scatter(
    popular["score"],
    popular["num_comments"],
    color="green",
    label="popular"
)

plt.title("score vs number of comments")
plt.xlabel("Score")
plt.ylabel("number of Comments")

plt.legend()
plt.savefig(
    "output/chart3_scatter.png",
    bbox_inches="tight"
)
plt.show()


fig, axes = plt.subplots(1, 3, figsize=(20, 7))

axes[0].barh(
    top10["short_title"],
    top10["score"]
)

axes[0].set_xlabel("Score")
axes[0].set_ylabel("Story Title")
axes[0].set_title("Top 10 Stories by Score")
axes[0].invert_yaxis()


axes[1].bar(
    category_counts.index,
    category_counts.values,
    color=plt.cm.tab10(range(len(category_counts)))
)

axes[1].set_title("Number of Stories by Category")
axes[1].set_xlabel("Category")
axes[1].set_ylabel("Number of Stories")

axes[1].tick_params(axis="x", rotation=45)


axes[2].scatter(
    non_popular["score"],
    non_popular["num_comments"],
    color="blue",
    label="Non-Popular"
)

axes[2].scatter(
    popular["score"],
    popular["num_comments"],
    color="green",
    label="Popular"
)

axes[2].set_title("Score vs Number of Comments")
axes[2].set_xlabel("Score")
axes[2].set_ylabel("Number of Comments")
axes[2].legend()


fig.suptitle("TrendPulse Dashboard", fontsize=18)

plt.tight_layout(rect=[0, 0, 1, 0.95])

plt.savefig(
    "output/dashboard.png",
    bbox_inches="tight"
)

plt.show()
