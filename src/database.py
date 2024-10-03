import os
from typing import TypedDict, Literal

from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

if not supabase_url or not supabase_key:
    raise ValueError(
        "Please provide SUPABASE_URL and SUPABASE_KEY environment variables"
    )

supabase = create_client(supabase_url, supabase_key)


class Article(TypedDict):
    updated_at: str
    journal: Literal["Wikinews", "Global Voices"]
    topic: str
    url: str
    title: str
    title_translated: str
    body: str
    body_translated: str
    language: str


def update_topics(journal: str, topics: tuple[str, ...]) -> None:
    for topic in map(lambda topic: {"name": topic, "journal": journal}, topics):
        supabase.table("topics").upsert(topic).execute()


def update_articles(articles: tuple[Article, ...]) -> None:
    for article in articles:
        supabase.table("articles").upsert(dict(article)).execute()
