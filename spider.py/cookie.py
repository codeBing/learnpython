__author__ = 'BING'
import cookielib,urllib,urllib2
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
url = 'http://www.qiushibaike.com/text'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36'}
try:
    request = urllib2.Request(url,headers =headers )
    response = opener.open(request)
    print response.read()
    for item in cookie:
        print 'Name = ', item.name
        print 'Value = ', item.value
except urllib2.URLError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

