import os
import sys
import json
import argparse
from CodeLoader import CodeLoader

class GenerateScript(object):

    def __init__(self):
        self.concept_codes = CodeLoader().load_code_from_html()


    def parse_args(self, args):
        parser = argparse.ArgumentParser(
            description="generate code for JQ")
        parser.add_argument(
            dest="template",
            help="the template to use in JQ, availables: [lsdb]",
            metavar="template")
        return parser.parse_args(args)


    def generate_code(self, filename):
        load_dir = './template'
        out_dir = '../tmp'
        read_path = os.path.join(os.path.dirname(__file__), load_dir)
        out_path = os.path.join(os.path.dirname(__file__), out_dir)
        try:
            pyfile = open(read_path + '/' + filename + '.py', 'r', encoding="utf-8")
            content = pyfile.read()
            content = content.replace('${codes}', json.dumps(self.concept_codes))
            with open(out_path + '/jqscript.py', 'w') as filehandle:
                filehandle.write(content)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    gs = GenerateScript()
    args = gs.parse_args(sys.argv[1:])
    gs.generate_code(args.template)