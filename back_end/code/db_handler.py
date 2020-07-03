from pymongo import MongoClient
import urllib.parse


class DBHandler:
    def __init__(self, config):
        self.config = config
        self.client = self.get_client()

    def get_client(self):

        username = urllib.parse.quote_plus(self.config["DB"]["User"])
        password = urllib.parse.quote_plus(self.config["DB"]["Password"])
        host = self.config["DB"]["Host"]

        connection_str = "mongodb://{}:{}@{}".format(username, password, host)
        print("Connecting to: {}".format(connection_str))
        return MongoClient(connection_str)

    def show_dbs(self):
        dbs = self.client.list_databases()
        for db in dbs:
            print("DataBase: {}".format(db))
