from flask import Flask, render_template
import scraping
import summary

app = Flask(__name__)


@app.route('/')
def index():

    original_contents = []
    titles = []

    mylist = scraping.scraping()

    for title, content in mylist:
        titles.append(title)
        original_contents.append(content)

    print(original_contents[0])

    summary_contents = summary.lexrank_summary()

    mylist = zip(titles, original_contents, summary_contents)
    return render_template('index.html', title='News Summary App', context=mylist)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
