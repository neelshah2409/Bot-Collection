import requests
import json
from flask import Flask, request, render_template

# Constants
API_KEY = '7cecaa58d6244a0b73104ba3'
API_URL = f'https://openexchangerates.org/api/latest.json?app_id={API_KEY}'

app = Flask(__name__)

def convert_currency(amount, source_currency, target_currency):
    # Make API request
    response = requests.get(API_URL)
    data = response.json()

    # Check if API request was successful
    if response.status_code == 200:
        # Get exchange rates from API response
        rates = data['rates']

        # Convert amount from source to target currency
        if source_currency in rates and target_currency in rates:
            converted_amount = amount * (rates[target_currency] / rates[source_currency])
            return converted_amount
        else:
            return None
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        source_currency = request.form['source_currency']
        target_currency = request.form['target_currency']

        converted_amount = convert_currency(amount, source_currency, target_currency)

        if converted_amount is not None:
            result = f'{amount} {source_currency} = {converted_amount} {target_currency}'
        else:
            result = 'Currency conversion failed.'

        return render_template('index.html', result=result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
