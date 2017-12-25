# -*- coding:utf-8 -*-
# this script is for qiushibaike

import urllib,urllib2
import re
import time,os
from PIL import Image as image
import  matplotlib.pyplot as plt
plt.axis('off')


headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 '
            'Safari/537.36',
    'Referer':'https://www.qiushibaike.com/',
}
originalurl = 'http://www.qiushibaike.com'
request = urllib2.Request(originalurl,headers = headers)


try:
    response = urllib2.urlopen(request)
    result = response.read()
except urllib2.URLError as e:
    print '请求出错，程序退出！'
    exit()


# handle the first returned result, and analyse where to go
togeturl = re.compile(r'<a href=\"(/article/\d+)')
resource_list = togeturl.findall(result)

# start to scrapy the jokes
try:
    sequrl = originalurl + resource_list.pop(0)
except IndexError as e:
    print '没有内容可被展示！程序退出！'
    exit()

picture_re = re.compile(r'<div class=\"thumb\">')
picture_getter = re.compile(r'<img src=\"//(.*)/(.*?)\"')
counter = ''
while not counter:
    if not sequrl:
        print '无内容可展示，程序退出！'
        exit()
    start = time.time()
    try:
        response = urllib2.urlopen(urllib2.Request(sequrl,headers = headers))
    except urllib2.HTTPError:
        if resource_list:
            sequrl = originalurl + resource_list.pop(0)
        else:
            sequrl = ''
        print '本次请求错误，内容重新请求中……本次耗时：{0}s\n'.format(time.time()-start)
        continue
    process = time.time()
    raw_content = response.read()


    content_re = r'<div class=\"content\">(.*?)</div>'
    raw_joke = re.search(content_re ,raw_content , re.S)
    #exhibite the joke
    if raw_joke:
        joke =  raw_joke.group(1).decode('utf-8')
        joke = joke.replace('\n','')
        joke = joke.replace('<br/>','\n')
        print joke
        try:
            p = picture_re.search(raw_content).end()
        except AttributeError:
            p = 0
        if p:
            pic_raw_url = picture_getter.search(raw_content[p:])
            pic_name = pic_raw_url.group(2)
            pic_url = 'http://' + pic_raw_url.group(1) + '/' + pic_name
            urllib.urlretrieve(pic_url,pic_name)
            im = image.open(pic_name)
            plt.imshow(im)
            plt.ion()
            plt.pause(0.1)
            plt.show()
                                                

    #find next joke
    link_searcher = r'<input type=\"hidden\" value = \"(/article/\d+)\" id=\'articleNextLink\' />'
    next_link = re.search(link_searcher,raw_content)
    if next_link:
        sequrl = originalurl + next_link.group(1)
    else:
        try:
            sequrl = originalurl + resource_list.pop(0)
        except IndexError as e:
            sequrl = ''
    
    counter = raw_input('\n\n\n\n\n请求时间：{0}s    处理时间：{1}s\n输入回车继续浏览……\n\n'.format(process-start,time.time()-process))
    if p:
        plt.close()
        os.remove(pic_name)
