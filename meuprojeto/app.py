from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contato")
def contato():
    return render_template('contato.html')

@app.route("/quemsomos")
def quemsomos():
    return render_template('quemsomos.html')

if __name__ == "__main__":
    app.run(port=5000,debug=True,use_debugger=False, use_reloader=False)