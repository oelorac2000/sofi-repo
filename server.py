from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return "<h1> Hello </h1>"

@app.route("/register_page")
def register_page():
    return render_template("register.html")


if __name__ == "__main__":
    host = "0.0.0.0"
    port = "80"
    app.run(host, port)
