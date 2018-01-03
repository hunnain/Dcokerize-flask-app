import os
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")

PORT = int( os.environ.get("PORT"))

app.run(host='0.0.0.0', port=PORT)
print("app is running on port ", PORT)

