#from flask import Flask, request, render_template
##from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes
from flask import flash

s = CurrencyCodes()
c = CurrencyRates()

def convert(currency_from, currency_to, amount):
    """logic for converting the currency"""
    symbol = s.get_symbol(currency_to)
    return f'{symbol} {round(c.convert(currency_from, currency_to, amount), 2)}'

def validate_currency(currency_code):
    """tests to see if fore_python.converter will raise an error and flashes a message if so"""
    try:
        rate = c.get_rates(currency_code)
        return 0
    except:
        flash(f'Error: {currency_code} is not a valid currency')
        return 1

# def validate_amount(amount):
#    if type(amount) != int or type(amount) != float
#        flash(f'Error: {amount} is not a valid amount')
