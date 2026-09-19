import requests
import time
import json
import os
from datetime import datetime

category = {
    "technology": "AI, software, tech, code, computer, data, cloud, API, GPU, LLM",
    "worldnews": "war, government, country, president, election, climate, attack, global",
    "sports": "NFL, NBA, FIFA, sport, game, team, player, league, championship",
    "science": "research, study, space, physics, biology, discovery, NASA, genome",
    "entertainment": "movie, film, music, Netflix, game, book, show, award, streaming"
}

story_list_url = "https://hacker-news.firebaseio.com/v0/topstories.json"

headers = {
    "User-Agent": "TrendPulse/1.0"
}

try:
    response = requests.get(
        story_list_url,
        headers=headers,
        timeout=10
    )
    story_ids = response.json()

except requests.RequestException as e:
    print("Failed to fetch top stories:", e)
    exit()
all_stories = []
collected_ids = set()
for category_name, keyword_string in category.items():
    keywords = [
        keyword.strip().lower()
        for keyword in keyword_string.split(",")
    ]
    category_count = 0
    for story_id in story_ids:
        if category_count >= 25:
            break
        if story_id in collected_ids:
            continue

        story_url = (
            f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        )
        try:
            story_response = requests.get(
                story_url,
                headers=headers,
                timeout=10
            )

            story = story_response.json()

        except requests.RequestException as e:
            print(
                f"Failed to fetch story {story_id}: {e}"
            )
            continue
        title = story.get("title", "")
        if not title:
            continue

        title_lower = title.lower()
        matched = False

        for keyword in keywords:

            if keyword in title_lower:
                matched = True
                break

        if not matched:
            continue
        story_data = {
            "post_id": story.get("id"),
            "title": story.get("title"),
            "category": category_name,
            "score": story.get("score", 0),
            "num_comments": story.get("descendants", 0),
            "author": story.get("by"),
            "collected_at": datetime.now().isoformat()
        }

        all_stories.append(story_data)

        collected_ids.add(story_id)

        category_count += 1

    time.sleep(2)

os.makedirs("data", exist_ok=True)


today = datetime.now().strftime("%Y%m%d")

filename = f"data/trends_{today}.json"

with open(filename, "w", encoding="utf-8") as file:

    json.dump(
        all_stories,
        file,
        indent=4,
        ensure_ascii=False
    )
