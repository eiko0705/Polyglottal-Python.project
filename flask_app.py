from flask import Flask, render_template, request
import scraping
import summary
import translate

app = Flask(__name__, static_folder="static")


@app.route('/', methods=["GET", "POST"])
def index():

    titles = []
    original_contents = []

    mylist = scraping.scraping()
    for title, content in mylist:
        titles.append(title)
        original_contents.append(content)

    summary_contents = summary.lexrank_summary()

    context = zip(titles, summary_contents, original_contents)

    if request.method == "POST":
        if request.form.get("click") == "Translate to Japanese":
            jp_translate = translate.summary_translate()
            return render_template('index.html', title='News Summary App', context=context, translate=jp_translate)

    elif request.method == "GET":
        return render_template('index.html', title='News Summary App', context=context)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
