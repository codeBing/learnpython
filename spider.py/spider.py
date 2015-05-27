# -*- coding:utf-8 -*-
__author__ = 'BING'

import urllib2
import re
import codecs

class QBTB:
    def __init__(self,):
        self.baseurl = 'http://www.qiushibaike.com/text/page/'
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36'
        self.headers = {'User-Agent':self.user_agent}

    def getpagenum(self,page):
        pattern = re.compile('<div.*?class="pagebar.*?<a.*?</a>.*?<a.*?</a>.*?<a.*?</a>.*?<a.*?</a>.*?<a.*?</a>.*?<a.*?>(.*?)</a>',re.S)
        items = re.findall(pattern,page)
        return items[0]

    def getpage(self,num):
        try:
            url = self.baseurl + str(num)
            request = urllib2.Request(url,headers = self.headers)
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8','ignore')
            return content
        except urllib2.URLError,e:
            return None

    def getcontent(self,page):
        pattern = re.compile('<div.*?class="author".*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?<div.*?class="content".*?>(.*?)<!--(.*?)-->.*?</div>.*?<span.*?<i.*?>(.*?)</i>',re.S)
        items = re.findall(pattern,page)
        with codecs.open('qb.txt','a','utf-8') as f:
            for item in items:
                content = item[0]+' '+item[2]+'\r\n'+item[1]+'\r\n'+item[3]+'\r\n'
                f.write(content)

    def start(self):
        page = self.getpage(1)
        if page==None:
            print 'No response!'
        else:
            pagenum = self.getpagenum(page)
            for x in range(1,int(pagenum)+1):
                page = self.getpage(x)
                self.getcontent(page)

qbtb = QBTB()
qbtb.start()