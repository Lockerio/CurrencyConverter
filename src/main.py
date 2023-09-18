import json
from flask import Flask, jsonify, request
from src.config import API_KEY
from src.converter import Converter


app = Flask(__name__)
converter = Converter()

@app.route("/convert")
def convert():
    # data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    # with open('data.json', 'w') as json_file:
    #     json.dump(data, json_file)
    currency_from = request.args["from"]
    currency_to = request.args["to"]
    value = float(request.args["value"])

    with open('data.json', 'r') as json_file:
        data = json_file.read()

    data_as_dict = json.loads(data)["Valute"]
    currency_from_value = data_as_dict[currency_from]["Value"]
    currency_from_nominal = data_as_dict[currency_from]["Nominal"]
    currency_to_value = data_as_dict[currency_to]["Value"]
    currency_to_nominal = data_as_dict[currency_to]["Nominal"]

    return {"Result": converter.convert(currency_from_value,
                                        currency_from_nominal,
                                        currency_to_value,
                                        currency_to_nominal,
                                        value)}


@app.route("/")
def main():
    # data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    # with open('data.json', 'w', encoding='utf-8') as json_file:
    #     json.dump(data, json_file)

    with open('data.json', 'r', encoding='utf-8') as json_file:
        data = json_file.read()

    date = json.loads(data)["Date"]
    data_as_dict = json.loads(data)["Valute"]
    output_data = {
        "Date": date,
        "Currencies": [
            {
                currency: {
                    "Name": description["Name"],
                    "To RUB": converter.convert_currency_to_rub(description["Nominal"], description["Value"])
                }
            }
            for currency, description in zip(data_as_dict.keys(), data_as_dict.values())
        ]
    }
    return jsonify(output_data)


if __name__ == '__main__':
    app.run(debug=True)
