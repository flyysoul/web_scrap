# coding=utf-8

import bs4
import urllib.request as urlre
import urllib.error as urler

html = urlre.urlopen("http://www.lagou.com/")
bsObj = bs4.BeautifulSoup(html, "lxml")

namelist = bsObj.findAll("li", {"class": "position_list_item"})
for name in namelist:
    print(name.get_text())

    #   findAll和find 定义
    #   findAll(tag,attributes,recursive,text,limit,keywords)
    #   find(tag,attributes,recursive,text,keywords)
    ## BeautifulSoup四种对象
    ##  1. BeautifulSoup对象 :bsObj
    ##  2. 标签Tag对象        :bsObj.div.h1
    ##  3. NavigableString对象    :表示标签里的文字
    ##  4. Comment对象            :html文档的注释标签
