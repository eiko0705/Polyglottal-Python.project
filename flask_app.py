from flask import Flask, render_template
import scraping

app = Flask(__name__)


@app.route('/')
def index():
    mylist = scraping.scraping()
    return render_template('index.html', title='News Summary App', context=mylist)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
