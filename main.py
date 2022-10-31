from hackernews import HackerNews


def main() -> None:
    for article in HackerNews().articlces:
        print(str(article))
        print()


if __name__ == "__main__":
    main()
