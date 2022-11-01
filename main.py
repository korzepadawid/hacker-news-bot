from hackernews import fetch_main_page, parse_articles_page
from twitter import merge_strings_within_chars_limit, TwitterClient

def main() -> None:
    try:
        page = fetch_main_page()
        articles = [str(article) for article in parse_articles_page(page=page)]
        tweets = merge_strings_within_chars_limit(strs=articles)
        twitter = TwitterClient()
        twitter.post_sequentially(texts=tweets)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
