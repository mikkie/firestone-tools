import os
import sys
import json
import argparse
from datetime import datetime, timedelta

class LoadData(object):

    def __init__(self):
        pass

    def parse_args(self, args):
        parser = argparse.ArgumentParser(
            description="load trade data to mongodb")
        parser.add_argument(
            dest="codes",
            help="the stock codes",
            metavar="codes")
        parser.add_argument(
            "-s",
            "--strategy",
            dest="strategy",
            help="i.e. basic, ydls",
            metavar="strategy")
        return parser.parse_args(args)


    def load_data(self, strategy, codes):
        load_dir = './template'
        out_dir = '../tmp'
        read_path = os.path.join(os.path.dirname(__file__), load_dir)
        out_path = os.path.join(os.path.dirname(__file__), out_dir)
        executeDate = datetime.now()
        json_data = []
        if executeDate.hour > 15:
            executeDate = executeDate + timedelta(days=1)
        executeDateStr = '{}-{}-{}'.format(executeDate.year, ('0' + str(executeDate.month))[-2:], ('0' + str(executeDate.day))[-2:])
        try:
            jsonfile = open(read_path + '/' + strategy + '.json', 'r', encoding="utf-8")
            template = jsonfile.read()
            jsfile = open(read_path + '/insert.js', 'r', encoding="utf-8")
            insert_template = jsfile.read()
            code_list = codes.split(',')
            for code in code_list:
                tmp_content = template.replace('${code}', code).replace('${executeDate}', executeDateStr)
                json_data.append(tmp_content)
            final_content = ','.join(json_data)
            final_content = insert_template.replace('${data}', final_content)
            with open(out_path + '/result.js', 'w', encoding="utf-8") as filehandle:
                filehandle.write(final_content)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    # # to debug in vscode uncomment this block
    # import ptvsd
    # # 5678 is the default attach port in the VS Code debug configurations
    # print("start debug on port 5678")
    # ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
    # ptvsd.wait_for_attach()
    ld = LoadData()
    args = ld.parse_args(sys.argv[1:])
    ld.load_data(args.strategy, args.codes)