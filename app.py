from flask import Flask, request, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
# from forex_python.converter import CurrencyRates, CurrencyCodes
from logic import convert, validate_currency


app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def show_homepage():
    """Show the currency conversion form """
    return render_template("form.html")


@app.route("/results")
def convert_currency():
    """validates the inputs and presents errors back on form.html or takes
    user to the results"""
    num_of_errors = 0
    #
    currency_from = request.args["converting_from"].upper()
    currency_to = request.args["converting_to"].upper()
    currency_from_errors = validate_currency(currency_from)
    currency_to_errors = validate_currency(currency_to)
    amount = request.args["amount"]
    try:
        amount = float(request.args["amount"])
    except:
        flash(f'Error: {amount} is not a valid amount')
        num_of_errors += 1
# I came up with a hack solution for this. I'd like to know the proper way to handle it.....
    # I have been trying to figure out how to use multiple flash messages, if the existence
    # of the flash messages (and therefore the errors (try/except statements)) is what determines
    # if I will redirect back to the form.html and show the flash messages or continue on
    # to the results page. I've seen examples of how to loop through multiple flash messages
    # but none on how to perform multiple operations and wait to decide where to redirect
    # based on how many messages there are (if any errors were raised)
    num_of_errors += currency_from_errors
    num_of_errors += currency_to_errors
    if num_of_errors > 0:
        return render_template('form.html')

    results = convert(currency_from, currency_to, amount)
    print('results== ', results)
    return render_template("results.html", results=results)
