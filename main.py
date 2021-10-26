from flask import app
from flask.app import Flask
from flask import render_template, request, flash, jsonify, redirect



app = Flask(__name__)


@app.route("/")
def index():
    name = request.args['name'] 
    elements = ['Jennie', 'Daniel', 'Analia', 'Peggy', 'Pepper']
    elements = sorted(elements)
    return render_template("index.html", name=name, elements=elements)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
