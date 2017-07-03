#coding: utf-8

import urllib2,urllib,os
env = 'c:\\Users\\Lucti\\Desktop\\' #抓取内容保存到文件的位置

url = 'http://baike.baidu.com/search/word?word=' #搜索引擎的URL
keyword = '中国象棋'
goal = urllib.quote(keyword)  #转码
headers = {
    'GET': url,
    'Host': 'baike.baidu.com',
    'Referer': 'http://baike.baidu.com/item/%E4%BA%8C%E5%8D%81/5455685?fromtitle=20&fromid=17560523',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }
#result = urllib2.urlopen( url + goal)
request = urllib2.Request( url + goal )

for item in headers:
    request.add_header( item , headers[item] )
result = urllib2.urlopen(request)

#正则部分，该部分内容设计为去除14对尖括号，包括首位置的尖括号
import re
standard = r'\<div\sclass\=\"para\"[\w\s\=\-\"]*\>(.+)\<\/div\>'
standard = re.compile( standard )
standard2 = r'([^\<]*)\<?[^\>]*\>?([^\<]*)\<?[^\>]*\>?([^\<]*)\<?[^\>]*\>?([^\<]*)\<?[^\>]*\>?([^\<]*)\<?[^\>]*\>?([^\<]*)\<?[^\>]*\>?([^\<]*)\<?[^\>]*\>?([^\<]*)\<?[^\>]*\>?([^\<]*)\<?[^\>]*\>?([^\<]*)\<?[^\>]*\>?([^\<]*)\<?[^\>]*\>?([^\<]*)\<?[^\>]*\>?([^\<]*)\<?[^\>]*\>?([^\<]*)\<?[^\>]*\>?'
standard2 = re.compile( standard2 )


assert os.path.exists(env)
with open(env + 'get.txt', 'w+') as k:
    for item in result.readlines():
        mid = standard.match(item)
        if mid:
            newm = standard2.match( mid.group(1) )
            if newm:
                k.write( ''.join(newm.groups()).replace('&quot;','"'))
            else:
                k.write('FAIL!!!!'+mid.group(1).replace('&quot;','"'))
            k.write('\n\n')


