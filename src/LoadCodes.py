import tushare as ts
import json
from pymongo import MongoClient

class LoadCodes(object):

    _MONFO_URL = '127.0.0.1'

    _DATA_DB = 'firestone'

    _COLLECTION = 'codes'

    def __init__(self):
        client = MongoClient(LoadCodes._MONFO_URL, 27017)
        self.data_db = client[LoadCodes._DATA_DB]
        code_df = ts.get_today_all()
        self.code_list = json.loads(code_df.to_json(orient='records'))
        self.data_db[LoadCodes._COLLECTION].insert(self.code_list)


if __name__ == "__main__":
    LoadCodes()