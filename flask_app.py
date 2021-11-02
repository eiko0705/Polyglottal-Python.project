from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    name = "Eiko"
    return render_template('index.html', title='flask test', name=name)


@app.route('/good')
def good():
    name = "Good"
    return name


if __name__ == "__main__":
    app.run(port=8000, debug=True)
