from flask import flash
# from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes, RatesNotAvailableError

codes = CurrencyCodes()
rates = CurrencyRates()


def convert(currency_from, currency_to, amount):
    """logic for converting the currency"""
    symbol = codes.get_symbol(currency_to)
    try:
        print('to, from, amt ==', currency_from, currency_to, amount)
        converted_amt = rates.convert(currency_from, currency_to, amount)
    except RatesNotAvailableError:
        return None
    return f'{symbol} {round(converted_amt, 2)}'


def validate_currency(currency_code):
    """tests to see if forex_python.converter will raise an error and flashes a message if so"""
    try:
        rate = rates.get_rates(currency_code)
        return 0
    except:
        flash(f'Error: {currency_code} is not a valid currency')
        return 1

# def validate_amount(amount):
#    if type(amount) != int or type(amount) != float
#        flash(f'Error: {amount} is not a valid amount')
