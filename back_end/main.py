import os
import json
import time

from code.bank_report import Bank_Report
from code.db_handler import DBHandler


def create_output_folder_structure(config):
    dirs = config["dirs"]
    for directory in dirs:
        if not os.path.exists(dirs[directory]):
            print("Creating Dir: {}".format(dirs[directory]))
            os.makedirs(dirs[directory])


# def get_meta(db_handler):
#     print("Getting Meta...")
#     meta_obj = list(db_handler.meta_collection.find())
#     if meta_obj == []:
#         meta_obj = {}
#     else:
#         meta_obj = meta_obj[0]
#     print("Meta: {}".format(meta_obj))
#     return meta_obj

def get_json(file_name):
    with open(file_name) as f:
        return json.load(f)


def dump_json(file_name, data):
    with open(file_name, "w") as f:
        return json.dump(data, f, indent=2)


def is_file_old(file_name):
    if os.path.exists(file_name):
        age = (time.time() - os.path.getmtime(file_name)) / 60
        if age > 20:
            print("File is {} min old".format(age))
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


def main():
    config = get_json("config.json")
    print("Config: {}".format(config))
    create_output_folder_structure(config)

    db_handler = DBHandler(config)
    report_handler = Bank_Report(config, db_handler)

    # Get Bank Links from RBI Home Page
    bank_links = get_bank_links(config, db_handler, report_handler)
    # meta_obj = get_meta(db_handler)
#     report_handler.update_meta()
#     print(meta_obj)
#     db_handler.meta_collection.replace_one({}, meta_obj)
#     _ = get_meta(db_handler)


if __name__ == '__main__':
    main()
