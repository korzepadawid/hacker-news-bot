import re
import requests

from typing import List
from bs4 import BeautifulSoup, ResultSet


HACKER_NEWS_URL = "https://news.ycombinator.com/"


class Article:
    """represents an article from the hacker news"""

    def __init__(self, url: str, title: str) -> None:
        self.url = url
        self.title = title

    def __str__(self) -> str:
        return f'{self.title} [{self.url}]'


class HNRequestError(Exception):
    """raised when the status code is different than 200 (OK)"""

    def __init__(self) -> None:
        super().__init__("failed to connect with the hacker news")


def fetch_main_page() -> bytes:
    """fetches the main page, otherwise raises an error"""
    response = requests.get(HACKER_NEWS_URL)
    if response.status_code != requests.codes.ok:
        raise HNRequestError()
    return response.content


def parse_articles_page(page: bytes) -> List[Article]:
    soup = BeautifulSoup(page, "html.parser")
    table_rows = soup.find_all("tr", {"class": "athing"})
    articles = []
    for row in table_rows:
        article = parse_article(row)
        articles.append(article)
    return articles


def parse_article(row: ResultSet) -> Article:
    title_section = row.find(
        "span", {"class": "titleline"}).find("a")
    url = title_section["href"]
    if is_relative_url(url):
        url = HACKER_NEWS_URL + url
    return Article(url=url, title=title_section.text)


RELATIVE_PATH_MATCHER = re.compile(r"""^                    # At the start of the string, ...
                   (?!                  # check if next characters are not...
                      www\.             # URLs starting with www.
                     |
                      (?:http|ftp)s?:// # URLs starting with http, https, ftp, ftps
                     |
                      [A-Za-z]:\\       # Local full paths starting with [drive_letter]:\  
                     |
                      //                # UNC locations starting with //
                   )                    # End of look-ahead check
                   .*                   # Martch up to the end of string""", re.X)


def is_relative_url(url: str) -> bool:
    return RELATIVE_PATH_MATCHER.search(url)
