import requests
from flask import Flask, jsonify, request
from src.utils.converter import Converter
from src.utils.validator import Validator

app = Flask(__name__)
converter = Converter()
validator = Validator()


@app.route("/convert")
def convert():
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

    currency_from = request.args["from"]
    currency_to = request.args["to"]
    value = request.args["value"]

    data_as_dict = data["Valute"]

    (currency_from_value,
     currency_from_nominal,
     currency_from_error_message) = validator.check_currency(currency_from, data_as_dict)
    if currency_from_error_message:
        return jsonify(currency_from_error_message)

    (currency_to_value,
     currency_to_nominal,
     currency_to_error_message) = validator.check_currency(currency_to, data_as_dict)
    if currency_to_error_message:
        return jsonify(currency_to_error_message)

    value, value_error_message = validator.check_value(value)
    if value_error_message:
        return jsonify(value_error_message)

    result = converter.convert(currency_from_value, currency_from_nominal,
                               currency_to_value, currency_to_nominal, value)
    return jsonify({"Result": result})


@app.route("/")
def main():
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    date = data["Date"]
    data_as_dict = data["Valute"]
    output_data = {
        "Date": date,
        "Currencies": [
            {
                currency: {
                    "Name": description["Name"],
                    "To RUB": converter.convert_currency_to_rub(description["Nominal"],
                                                                description["Value"])
                }
            }
            for currency, description in zip(data_as_dict.keys(), data_as_dict.values())
        ]
    }
    return jsonify(output_data)


if __name__ == '__main__':
    app.run(debug=True)
