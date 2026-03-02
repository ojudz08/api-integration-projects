"""
    Fetch news from NewsAPI (https://newsapi.org/) which is a simple HTTP REST API for searching and fetching articles from the web
    Date Created: March 1, 2026
"""

import os
import pandas as pd
from dotenv import load_dotenv
from newsapi import NewsApiClient
from datetime import datetime

# Load environment variables
load_dotenv()


class NewsFetcher:
    def __init__(self, search_keyword, file_name):
        self.api_key = self.get_api_key()
        self.newsapi_url = 'https://newsapi.org/v2'
        self.keyword = search_keyword
        self.file_name = file_name


    def get_api_key(self):
        """Access news api key using os.getenv"""
        newsapi_key = os.getenv("NEWSAPI_API_KEY")

        if newsapi_key:
            api = NewsApiClient(api_key=newsapi_key)
            return api
        else:
            print("Error: API Key not found. Check your .env file.")
            print("Get your api key at https://newsapi.org/")


    def get_everything(self, range_dt):
        """Search through millions of articles"""

        from_dt, to_dt = range_dt[0], range_dt[1]
        
        tmp_nws = []
        for pg_i in range(1, 100):
            tmp_dict = self.api_key.get_everything(q=self.keyword, from_param=from_dt, to=to_dt, language='en', page=pg_i)
            tmp_news_articles = tmp_dict['articles']

            if len(tmp_news_articles) > 0:
                tmp_nws = tmp_nws + tmp_news_articles
            else:
                break

        news_articles = tmp_nws

        return self.save_as_csv(news_articles)

    
    def get_top_headlines(self, src, cntry, ctgry):
        """Search the life top and breaking headlines for a country, specific category, single or multiple source"""

        tmp_nws = []
        for pg_i in range(1, 100):
            tmp_dict = self.api_key.get_top_headlines(q=self.keyword, sources=src, language='en', country=cntry, category=ctgry, page=pg_i)
            tmp_news_articles = tmp_dict['articles']

            if len(tmp_news_articles) > 0:
                tmp_nws = tmp_nws + tmp_news_articles
            else:
                break

        news_articles = tmp_nws

        return self.save_as_csv(news_articles)


    def save_as_csv(self, news_dict):
        news_articles = news_dict
        headline, author, source, published_dt, url = [], [], [], [], []

        for item in range(0, len(news_articles)):
            news_headline = news_articles[item]['title']
            news_author = news_articles[item]['author']
            news_source = news_articles[item]['source']['name']
            news_published_dt = datetime.fromisoformat(news_articles[item]['publishedAt'].replace('Z', '+00:00')).strftime("%Y-%m-%d %I:%M %p")
            news_url = news_articles[item]['url']

            headline.append(news_headline)
            author.append(news_author)
            source.append(news_source)
            published_dt.append(news_published_dt)
            url.append(news_url)
        
        column_names = ["Headlines", "Author", "Source", "Published Date", "News Url"]
        data_df = pd.DataFrame(list(zip(headline, author, source, published_dt, url)), columns=column_names)

        file_path = os.path.join(os.getcwd() + "/data/", self.file_name)
        data_df.to_csv(file_path, index=False)
        
        return f"Data saved as {self.file_name}.csv!"


if __name__ == '__main__':
    search_keyword = "iran"
    range_dt = ["2026-02-21", "2026-02-21"]
    file_name = f"{search_keyword}_newsoutput.csv"
    fetch_news = NewsFetcher(search_keyword, file_name)
    test = fetch_news.get_everything(range_dt)

    # src = "ABC News"
    # cntry = "us"
    # ctgry = "health"  # business, entertainment, general, health, science, sports, technology
    # test = fetch_news.get_top_headlines(src, cntry, ctgry)
    
    print(test)
