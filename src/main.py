import codecs
import json

import requests
from flask import Flask, jsonify
from src.config import API_KEY

app = Flask(__name__)


@app.route("/convert")
def convert():
    # data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    # with open('data.json', 'w') as json_file:
    #     json.dump(data, json_file)

    with open('data.json', 'r') as json_file:
        data = json_file.read()

    data_as_dict = json.loads(data)
    return data_as_dict


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
                    "To RUB": description["Value"]
                }
            }
            for currency, description in zip(data_as_dict.keys(), data_as_dict.values())
        ]
    }
    return jsonify(output_data)


if __name__ == '__main__':
    app.run(debug=True)
