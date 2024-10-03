from typing import TypedDict
import time


class TitleDetail(TypedDict):
    type: str
    language: str
    base: str
    value: str


class Link(TypedDict):
    rel: str
    type: str
    href: str


class SummaryDetail(TypedDict):
    type: str
    language: str
    base: str
    value: str


class AuthorDetail(TypedDict):
    name: str


class Article(TypedDict):
    id: str
    guidislink: bool
    link: str
    title: str
    title_detail: TitleDetail
    links: list[Link]
    updated: str
    updated_parsed: time.struct_time
    summary: str
    summary_detail: SummaryDetail
    authors: list[dict[str, str]]
    author_detail: AuthorDetail
    author: str


class Target(TypedDict):
    language: str
    endpoint: str
    topics: tuple[str, ...]
