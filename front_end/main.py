from flask import Flask, render_template
import json

from db_handler import DBHandler

app = Flask(__name__)


def get_json(file_name):
    with open(file_name) as f:
        return json.load(f)


config = get_json("config.json")
db_handler = DBHandler(config)


@app.route('/')
def home():
    data = db_handler.fetch_data(config["DB"]["bank_links"])
    return render_template('home.html', data=data)


@app.route('/banks')
def list_banks():
    data = db_handler.fetch_data(config["DB"]["bank_links"])
    return render_template('bank_list.html', data=data)


@app.route('/bank/<bank_name>')
def bank(bank_name):
    bank_name = bank_name.replace("%20", "_").replace(" ", "_")
    print(bank_name)
    data = db_handler.fetch_data(bank_name)
    print(data)
    return render_template('bank.html', bank_name=bank_name, data=data)
