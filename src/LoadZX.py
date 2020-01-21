import argparse
import sys
from pymongo import MongoClient

class LoadZX(object):

    _MONFO_URL = '127.0.0.1'

    _DATA_DB = 'firestone'

    _COLLECTION = 'zx'

    def __init__(self, codes):
        self.codes = codes
        client = MongoClient(LoadZX._MONFO_URL, 27017)
        data_db = client[LoadZX._DATA_DB]
        self.concepts = data_db['concepts']
        self.zx = data_db['zx']


    def load_zx(self):
        for code in self.codes.split(','):
            stocks = list(self.concepts.find({"code" : code}))
            if(len(stocks) == 1):
                stock = stocks[0]
                for key, value in stock['concepts'].items():
                    concept = list(self.zx.find({"concept" : value}))
                    if(len(concept) > 0):
                        exists_codes = concept[0]['codes']
                        exists_codes.append(code)
                        exists_codes = list(set(exists_codes))
                        self.zx.update_one({"_id" : concept[0]['_id']}, {'$set' : {'codes' : exists_codes}})
                    else:
                        self.zx.insert_one({'concept' : value, 'codes' : [code]})

    @staticmethod
    def parse_args(args):
        parser = argparse.ArgumentParser(
            description="load zx data to mongodb")
        parser.add_argument(
            dest="codes",
            help="the stock codes",
            metavar="codes")
        return parser.parse_args(args)


if __name__ == "__main__":
    # # to debug in vscode uncomment this block
    # import ptvsd
    # # 5678 is the default attach port in the VS Code debug configurations
    # print("start debug on port 5678")
    # ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
    # ptvsd.wait_for_attach()
    args = LoadZX.parse_args(sys.argv[1:])
    lzx = LoadZX(args.codes)
    lzx.load_zx()