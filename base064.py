import base64

def smart_en(s):
    if not isinstance(s,str):
        raise TypeError('a string is expected!!!!!!!!')
    mid = base64.b64encode(s)
    L = len(mid)
    for i in xrange(1,4):
        if mid[-i]!='=':
            return mid[:-i]+mid[-i]

def smart_de(s):
    if not isinstance(s,str):
        raise TypeError('a str is expected, please check the variable!!!!!!')
    rest = len(s)% 4
    mid = s
    if rest != 0:
        mid = s + '=' * (4-rest)
    return base64.b64decode(mid)

if __name__ == '__main__':
    abc = 'sdssdsd'
    ni =  smart_en(abc)
    print smart_de(ni)