from flask import Flask, render_template
import scraping
import summary

app = Flask(__name__, static_folder="static")


@app.route('/')
def index():

    titles = []
    original_contents = []

    mylist = scraping.scraping()

    for title, content in mylist:
        titles.append(title)
        original_contents.append(content)

    summary_contents = summary.lexrank_summary()

    mylist = zip(titles, summary_contents, original_contents)
    return render_template('index.html', title='News Summary App', context=mylist)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
