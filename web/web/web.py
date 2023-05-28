from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/picture')
def picture():
    return render_template('picture.html')

if __name__ == "__main__":
   app.run(debug = False)
