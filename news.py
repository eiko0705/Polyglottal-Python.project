from typing import Counter
from newsapi import NewsApiClient

# initialize client
newsapi = NewsApiClient(api_key='37fc69d716d14e20a12378ea93681428')

# get the headline news from the site assigned at sources
headlines = newsapi.get_top_headlines(sources='techcrunch')

# display one of the news that I got
# print(headlines['articles'][0])

print(headlines['articles'][0]['author'])
print(headlines['articles'][0]['content'])
