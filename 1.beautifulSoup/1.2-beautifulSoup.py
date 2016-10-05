# coding=utf-8

import bs4
import urllib.request as urlre
import urllib.error as urler

html = urlre.urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj = bs4.BeautifulSoup(html, "lxml")
# print(bsObj)
try:
    bad = bsObj.nothing.tag
except AttributeError as e:
    print("tag was not fount")
else:
    if bad == None:
        print("tag`s content is none")
    else:
        print(bad)


def getTitle(url):
    try:
        html = urlre.urlopen(url)
    except (urler.HTTPError, urler.URLError) as e:
        return None
    try:
        bsObj = bs4.BeautifulSoup(html, "lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return None


title = getTitle("https://www.zhihu.com/")
if title == None:
    print("could not be found")
else:
    print(title)
