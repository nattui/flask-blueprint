# Flask Application

from flask import Flask, render_template
app = Flask(__name__)

name = "John Smith"

# http://127.0.0.1:5000/
@app.route("/")
def index():
    name = "John"
    return render_template("index.html", name = name)

# http://127.0.0.1:5000/information
@app.route("/info")
def info():
    return render_template("info.html", name = name)

print("Hello", "Smith")

if __name__ == "__main__":
    app.run(debug = True)
