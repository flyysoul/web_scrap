# -*- coding=utf-8 -*-

import urllib.request as urlre
import bs4
import re

html = urlre.urlopen("http://www.lagou.com/zhaopin/Python/?labelWords=label")
bsObj = bs4.BeautifulSoup(html, "lxml")
images = bsObj.findAll("img", {"src": re.compile("\/\/www\.lgstatic\.com.*\.(jpg|png)")})
for image in images:
    # print(image.attrs)
    print(image["src"], image.attrs["src"])
# Lambda表达式
images = bsObj.findAll(lambda tag: len(tag.attrs) == 2)