# -*-coding=utf-8-*-
__author__ = 'aqua'

import os
import re
from lxml import etree


class CodeLoader(object):

    def load_code_from_html(self):
        load_dir = '../data/html'
        path = os.path.join(os.path.dirname(__file__), load_dir)
        codes = []
        for file in os.listdir(path):
            try:
                htmlf = open(path + '/' + file, 'r', encoding="utf-8")
                htmlcont = htmlf.read()
                page = etree.HTML(htmlcont)
                trs = page.xpath('//table/tr')
                i = 0
                while i < len(trs):
                    code = trs[i].getchildren()[0].text.strip()
                    if re.match('^\d{6}.(SH|SZ)$', code) is not None:
                        code = code.replace('.SH', '').replace('.SZ', '')
                        if code not in codes:
                            codes.append(code)
                    i += 1
            except Exception as e:
                print('failed to read %s, e=%s' % (file, e))
        return codes


if __name__ == "__main__":
    print(CodeLoader().load_code_from_html())
