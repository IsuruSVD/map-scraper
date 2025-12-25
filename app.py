from flask import Flask, render_template, request
from scraper import run_scraper

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    file_path = None

    if request.method == "POST":
        category = request.form["category"]
        area = request.form["area"]
        file_path = run_scraper(category, area)

    return render_template("index.html", file_path=file_path)

if __name__ == "__main__":
    app.run(debug=True)
