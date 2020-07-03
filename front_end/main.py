from flask import Flask, render_template
import json

from db_handler import DBHandler

app = Flask(__name__)


def get_json(file_name):
    with open(file_name) as f:
        return json.load(f)


@app.route('/')
def home():
    return "Hello To The world!"


config = get_json("config.json")
db_handler = DBHandler(config)


@app.route('/banks')
def banks():
    # data = [
    #     {
    #         "name": "Abhyudaya Cooperative Bank",
    #         "link": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_02.xlsx"
    #     }
    # ]
    data = db_handler.fetch_data(config["DB"]["bank_links"])
    return render_template('bank_list.html', data=data)
