import os
import json
import time
import urllib.request
import pandas

from code.bank_report import Bank_Report
from code.db_handler import DBHandler


def create_output_folder_structure(config):
    dirs = config["dirs"]
    for directory in dirs:
        if not os.path.exists(dirs[directory]):
            print("Creating Dir: {}".format(dirs[directory]))
            os.makedirs(dirs[directory])


def get_json(file_name):
    with open(file_name) as f:
        return json.load(f)


def dump_json(file_name, data):
    with open(file_name, "w") as f:
        return json.dump(data, f, indent=2)


def is_file_old(file_name):
    if os.path.exists(file_name):
        age = int(time.time() - os.path.getmtime(file_name)) // (60 * 60)
        if age > 24:  # If file is one day old
            print("File is {} hours old".format(age))
            return True
    else:
        return True
    return False


def get_bank_links(config, db_handler, report_handler):
    file_name = config["bank_links_file"]
    if is_file_old(file_name):
        print("Updating Bank Links")
        rbi_content = report_handler.downlad_rbi_page()
        bank_links = report_handler.get_bank_links_from_HTML(rbi_content)
        dump_json(file_name, bank_links)
        return bank_links
    return get_json(file_name)


def download_bank_report(file_path, url):
    if is_file_old(file_path):
        print("Downloading file: {}".format(file_path))
        urllib.request.urlretrieve(url, file_path)


def parse_bank_report(xlsx_file_path, json_file_path):
    parsed = False
    json_str = ""
    if is_file_old(json_file_path):
        print("Parsing file: {}".format(xlsx_file_path))
        excel_data_df = pandas.read_excel(xlsx_file_path)
        json_str = excel_data_df.to_json(orient='records')
        with open(json_file_path, "w") as jf:
            json.dump(json_str, jf)
        parsed = True
    return parsed, json_str


def main():
    config = get_json("config.json")
    print("Config: {}".format(config))
    create_output_folder_structure(config)

    db_handler = DBHandler(config)
    report_handler = Bank_Report(config, db_handler)

    # Get Bank Links from RBI Home Page
    bank_links = get_bank_links(config, db_handler, report_handler)
    db_handler.refresh(config["DB"]["bank_links"], bank_links)

    for bank_link in bank_links:
        # print(bank_link)
        bank_file_path = "{}/{}.xlsx".format(
            config["dirs"]["out_dir_bank_reports"],
            bank_link["name"].replace(" ", "_")
        )
        download_bank_report(bank_file_path, bank_link["link"])

        json_file_path = "{}/{}.json".format(
            config["dirs"]["json_reports_dir"],
            bank_link["name"].replace(" ", "_")
        )
        parsed, json_str = parse_bank_report(bank_file_path, json_file_path)

        if parsed:
            collection_name = bank_link["name"].replace(" ", "_")
            json_data = json.loads(json_str)
            db_handler.refresh(collection_name, json_data)


if __name__ == '__main__':
    main()
