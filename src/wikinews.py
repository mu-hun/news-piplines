from typing import Final
from urllib.parse import urlencode

import database
import wikinews_type

import feedparser  # type: ignore

from utils import flatmap

targets: Final[tuple[wikinews_type.Target, ...]] = (
    {
        "language": "english",
        "endpoint": "https://en.wikinews.org/w/index.php",
        "topics": (
            "Politics_and_conflicts",
            "Disasters_and_accidents",
            "Economy_and_business",
            "Science_and_technology",
            "Culture_and_entertainment",
            "Health",
            "Environment",
            "Crime_and_law",
            "Sports",
            "Obituaries",
        ),
    },
    {
        "language": "japanese",
        "endpoint": "https://ja.wikinews.org/w/index.php",
        "topics": ("政治", "経済", "社会", "文化", "スポーツ", "学術", "気象"),
    },
)


default_params: Final = {
    "title": "Special:NewsFeed",
    "feed": "atom",
    "notcategories": "No publish|Archived|AutoArchived|disputed",
    "namespace": "0",
    "count": "30",
    "ordermethod": "categoryadd",
    "stablepages": "only",
}


def get_news_feed(target: wikinews_type.Target) -> tuple[database.Article, ...]:
    endpoint = target["endpoint"]
    topics = target["topics"]
    language = target["language"]

    def get_articles_by_topic(topic: str) -> tuple[database.Article, ...]:
        params = default_params.copy()
        params["categories"] = f"{topic}"

        url = f"{endpoint}?{urlencode(params)}"
        articles: list[wikinews_type.Article] = feedparser.parse(url).entries

        def convert(article: wikinews_type.Article) -> database.Article:
            return {
                "updated_at": article["updated"],
                "journal": "Wikinews",
                "topic": topic,
                "url": article["id"],
                "title": article["title"],
                "body": article["summary"],
                # TODO: Translate title and body
                "title_translated": "",
                "body_translated": "",
                "language": language,
            }

        return tuple(map(convert, articles))

    return flatmap(get_articles_by_topic, topics)


def main() -> None:
    for target in targets:
        database.update_topics("Wikinews", target["topics"])
        database.update_articles(get_news_feed(target))
