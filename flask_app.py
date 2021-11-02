from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)


@app.route('/')
def index():
    # initialize client
    newsapi = NewsApiClient(api_key='37fc69d716d14e20a12378ea93681428')

    # get the headline news from the site assigned at sources
    headlines = newsapi.get_top_headlines(sources='techcrunch')

    articles = headlines['articles']

    content = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        content.append(myarticles['content'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, content, img)

    return render_template('index.html', title='News Summary App', context=mylist)


@app.route('/good')
def good():
    name = "Good"
    return name


if __name__ == "__main__":
    app.run(port=8000, debug=True)
