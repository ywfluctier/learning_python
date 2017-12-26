import urllib,urllib2
import re


homepage_url = 'https://www.zhihu.com/people/adshaw/activities'
username = 'example'
response = urllib2.urlopen( homepage_url )
raw_content = response.read()

avatar_re = re.compile('<img class=\"Avatar Avatar--large UserAvatar-inner\" width=\"160\" height=\"160\" src=\"(.*?)\" srcset=\"(.*?)\s(.*?)\" data-reactid=\"60\"/>')
avatar_getter = avatar_re.search(raw_content)
if avatar_getter:
    pic_url = avatar_getter.group(2)
    if 'jpg' in pic_url[-10:]:
        pic_name = username + '.jpg'
    elif 'png' in pic_url[-10:]:
        pic_name = username + '.png'
    else:
        pic_name = username + '.xxx'
    try:
        raw_avatar = urllib2.urlopen(pic_url)
    except urllib2.HTTPError as e:
        print e.reason
        exit()
        
        try:
            pic_url = avatar_getter.group(1)
            pic_name = 'x_' + pic_name
            raw_avatar = urllib2.urlopen(pic_url)
        except urllib2.HTTPError:
            exit()
    with open(pic_name,'wb') as f:
        f.write(raw_avatar.read())
