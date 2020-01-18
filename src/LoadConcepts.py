import tushare as ts
import json
import requests
import random
import time
import argparse
import sys
from lxml import etree
from pymongo import MongoClient

class LoadConcepts(object):

    _MONFO_URL = '127.0.0.1'

    _DATA_DB = 'firestone'

    _COLLECTION = 'codes'

    def __init__(self, in_codes):
        self.__header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': '__utma=156575163.1101180334.1557107567.1574493865.1575014992.6; __utmz=156575163.1575014992.6.3.utmcsr=yamixed.com|utmccn=(referral)|utmcmd=referral|utmcct=/fav/article/2/157; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1574645288,1574668383,1575015038,1575876694; reviewJump=nojump; searchGuide=sg; usersurvey=1; v=AlpMfC4B0FNi31z_cQ8I2alwqwt_i95kUA9SCWTTBu241_Q9TBsudSCfoh03',
            'Host': 'basic.10jqka.com.cn',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        }
        client = MongoClient(LoadConcepts._MONFO_URL, 27017)
        self.data_db = client[LoadConcepts._DATA_DB]
        if(in_codes is not None):
            self.code_list = [{'code' : code} for code in in_codes.split(',')]
        else:
            self.code_list = self.data_db[LoadConcepts._COLLECTION].find({})

    def load_concepts(self):
        error_codes = []
        for code_json in self.code_list:
            code = code_json['code']
            try:
                json_data = self.get_concept(code)
                self.data_db['concepts'].insert(json_data)
                inter = int(random.random() * 3) + 2
                time.sleep(inter)
            except Exception:
                error_codes.append(code)
        if(len(error_codes) > 0):
            print(f"get F10 data error: {','.join(error_codes)}")

    def get_concept(self, code):
        concept_json = {
            'code' : code, 
            'concepts' : {}
        }
        info = {
            'name' : '/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/h1',
            'type' : '//*[@id="profile"]/div[2]/table[2]/tbody/tr[1]/td[4]/span[2]',
            'xsjj' : '//*[@id="profile"]/div[2]/table[2]/tbody/tr[6]/td[1]/span[2]',
            'hy' : '//*[@id="profile"]/div[2]/table[1]/tbody/tr[1]/td[2]/span[2]',
            'main_business' : '//*[@id="profile"]/div[2]/table[1]/tbody/tr[1]/td[1]/span[2]/a',
            'pe' : '//*[@id="dtsyl"]'
        }
        response = requests.get(f'http://basic.10jqka.com.cn/{code}/',headers=self.__header)
        response.encoding = response.apparent_encoding
        page = etree.HTML(response.text)
        for key in info:
            try:    
                concept_json[key] = page.xpath(info[key])[0].text.strip()
            except Exception:
                concept_json[key] = ''
        concepts = page.xpath('//*[@id="profile"]/div[2]/table[1]/tbody/tr[2]/td/div[2]')
        if(len(concepts) == 0):
            concepts = page.xpath('//*[@id="profile"]/div[2]/table[1]/tbody/tr[2]/td/div')
        for index, cont in enumerate(concepts[0].getchildren()):
            if(index < len(concepts[0]) - 1):
                concept_json['concepts'][str(index)] = cont.text.strip()
        return concept_json


    @staticmethod
    def parse_args(args):
        parser = argparse.ArgumentParser(
            description="load concept data to mongodb")
        parser.add_argument(
            dest="codes",
            help="the stock codes",
            nargs="?",
            metavar="codes")
        return parser.parse_args(args)
        


if __name__ == "__main__":
    # # to debug in vscode uncomment this block
    # import ptvsd
    # # 5678 is the default attach port in the VS Code debug configurations
    # print("start debug on port 5678")
    # ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
    # ptvsd.wait_for_attach()
    args = LoadConcepts.parse_args(sys.argv[1:])
    lc = LoadConcepts(args.codes)
    lc.load_concepts()

