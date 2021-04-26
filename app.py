from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

@app.route("/results")
def convert_currency():

    currency_from = request.args["converting_from"]
    currency_to = request.args["converting_to"]
    amount = request.args["amount"]
