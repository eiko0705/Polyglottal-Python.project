import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import time
import urllib.request
import urllib.error
import re


def scraping():

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

        # Reading the title
        title_with_tag = soup_article.find('h1')
        title = title_with_tag.get_text()
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
    return mylist


scraping()

if __name__ == '__main__':
    scraping()
