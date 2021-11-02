from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import time
import urllib.request
import urllib.error
import re

app = Flask(__name__)


# I've changed the way to get the article data from api to scraping
# I'll keep this code for the future

# @app.route('/')
# def index():

# # initialize client
# newsapi = NewsApiClient(api_key='37fc69d716d14e20a12378ea93681428')

# # get the headline news from the site assigned at sources
# headlines = newsapi.get_top_headlines(sources='techcrunch')

# articles = headlines['articles']

# content = []
# news = []
# img = []

# for i in range(len(articles)):
#     myarticles = articles[i]

#     news.append(myarticles['title'])
#     content.append(myarticles['content'])
#     img.append(myarticles['urlToImage'])

# mylist = zip(news, content, img)

# return render_template('index.html', title='News Summary App', context=mylist)

# url definition
url = "https://www.japantimes.co.jp/"

# create array for storing each article href
list_links = []

html_page = urllib.request.urlopen(url)
soup = BeautifulSoup(html_page, 'html5lib')
for link in soup.find_all('a', class_='top-story'):
    list_links.append(link.get('href'))

# Empty lists for content, links and titles
news_contents = []
list_titles = []

for link in list_links:
    article = requests.get(link)
    article_content = article.content
    soup_article = BeautifulSoup(article_content, 'html5lib')

    # Reading the content (it is divided in paragraphs)
    title = soup_article.find('h1')
    list_titles.append(title)

    # Reading the content (it is divided in paragraphs)
    body = soup_article.find_all('div', class_='entry')
    x = body[0].find_all('p')

    # Unifying the paragraphs
    list_paragraphs = []
    for p in np.arange(0, len(x)):
        paragraph = x[p].get_text()
        list_paragraphs.append(paragraph)
        final_article = " ".join(list_paragraphs)

    news_contents.append(final_article)

mylist = zip(list_titles, news_contents)


@app.route('/')
def index():

    return render_template('index.html', title='News Summary App', context=mylist)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
