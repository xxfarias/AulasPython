from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/quemSomos")
def quemSomos():
    return render_template("quemSomos.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
