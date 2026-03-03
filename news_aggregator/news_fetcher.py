"""
    Fetch news from NewsAPI (https://newsapi.org/) - a simple HTTP REST API for news articles from the web
    Date Created: March 1, 2026
"""

import os, logging
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from newsapi import NewsApiClient
from datetime import datetime

# Save logs to file and prints them
logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s -- %(message)s",
    datefmt = "%Y-%m-%d %I:%M %p",
    handlers = [
        logging.FileHandler(Path("./logs") / "news_fetcher_logs.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()


class NewsFetcher:
    def __init__(self, file_name: str):
        self.api_key = os.getenv("NEWSAPI_API_KEY")
        if not self.api_key:
            logger.error(f"API Key missing in .env file.")
            raise ValueError("API Key not found. Please set NEWSAPI_API_KEY in your .env file.")

        self.newsapi_client = NewsApiClient(api_key=self.api_key)
        self.file_name = file_name
        self.data_dir = Path("./data")
        self.data_dir.mkdir(exist_ok=True)

    
    def _fetch_paginated_articles(self, method_name: str, **kwargs) -> list:
        """Handle pagination up to 5 pages due to API limit for developer plan."""

        all_articles = []

        try:
            for pg_i in range(1, 6):
                method = getattr(self.newsapi_client, method_name)
                response = method(**kwargs, page=pg_i)

                articles = response.get('articles', [])
                if not articles: break

                all_articles.extend(articles)
                logger.info(f"Fetched page {pg_i} for {method_name} method...")

        except Exception as e:
            logger.error(f"Failed to fetch news for {method_name} method: {e}")
        
        return all_articles


    def get_everything(self, keyword: str, date_range: list):
        """Search through millions of articles by keyword and date."""

        news_articles = self._fetch_paginated_articles(
            'get_everything',
            q = keyword,
            from_param = date_range[0],
            to = date_range[1],
            language = 'en'
        )

        return self.save_as_csv(news_articles)

    
    def get_top_headlines(self, country: str, category: str):
        """Search the life top and breaking headlines for a country and specific category"""

        news_articles = self._fetch_paginated_articles(
            'get_top_headlines',
            country = country,
            category = category,
            language = 'en'
        )

        return self.save_as_csv(news_articles)


    def save_as_csv(self, articles: list) -> str:
        """Transform the dict data into dataframe and save as csv"""
        if not articles:
            logger.warning("No articles found. CSV will not be created.")
            return "No data found."

        processed_news_data = []
        for art in articles:
            processed_news_data.append({
                "Headline": art.get('title'),
                "Author": art.get('author'),
                "Source": art.get('source', {}).get('name'),
                "Published Date": datetime.fromisoformat(
                    art['publishedAt'].replace('Z', '+00:00')
                ).strftime("%Y-%m-%d %I:%M %p"),
                "News Url": art.get('url')
            })
        
        data_df = pd.DataFrame(processed_news_data)
        file_path = self.data_dir / self.file_name
        data_df.to_csv(file_path, index=False)
        logger.info(f"File saved successfully: {file_path}")
        
        return f"Successfully saved {len(data_df)} articles to {file_path}"


def get_inputs():
    """Prompt user for inputs"""
    print("\n--- NewsAPI Fetcher ---")
    print("1. Search Everything (Keyword)")
    print("2. Top Headlines (Category/Country)")
    choice = input("Select mode (1 or 2): ")

    if choice == '1':
        keyword = input("Enter search keyword: ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        return "everything", {"keyword": keyword, "date_range": [start_date, end_date]}

    else:
        country = input("Enter country code (e.g., 'us'): ")
        category = input("Enter category (e.g., 'health'): ")
        return "headlines", {"country": country, "category": category}


if __name__ == '__main__':
    file_name = "news_report.csv"
    fetcher = NewsFetcher(file_name)
    
    mode, params = get_inputs()

    if mode == "everything":
        result = fetcher.get_everything(**params)
    else:
        result = fetcher.get_top_headlines(**params)

    print(f"\n[Status]: {result}")
    print("Please check the 'news_fetcher.log' for execution details.")  
