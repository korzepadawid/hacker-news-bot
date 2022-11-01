from hackernews import fetch_main_page, parse_articles_page


def main() -> None:
    try:
        page = fetch_main_page()
        articles = parse_articles_page(page=page)
        for article in articles:
            print(str(article))
            print()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
