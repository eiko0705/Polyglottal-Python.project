import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import time
import urllib.request
import urllib.error
import re


# url definition
url = "https://www.japantimes.co.jp/"

# # request
# r = requests.get(url)
# r.status_code

# # save into the coverpage variable
# coverpage = r.content

# # soup creation
# soup = BeautifulSoup()

# # news indentification
# coverpage_news = soup.find_all('a', class_='top-story')

# print(coverpage_news[0])
list_links = []

html_page = urllib.request.urlopen(url)
soup = BeautifulSoup(html_page, 'html5lib')
for link in soup.find_all('a', class_='top-story'):
    list_links.append(link.get('href'))


# Empty lists for content, links and titles
news_contents = []
list_titles = []

for link in list_links:

    # Reading the content (it is divided in paragraphs)
    article = requests.get(link)
    article_content = article.content
    soup_article = BeautifulSoup(article_content, 'html5lib')
    body = soup_article.find_all('div', class_='entry')
    x = body[0].find_all('p')

    # Unifying the paragraphs
    list_paragraphs = []
    for p in np.arange(0, len(x)):
        paragraph = x[p].get_text()
        list_paragraphs.append(paragraph)
        final_article = " ".join(list_paragraphs)

    news_contents.append(final_article)


print(news_contents[3])
