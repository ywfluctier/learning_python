#coding:utf-8
import re,os

CON = '.MID'
path = r'E:\mid3'
assert os.path.exists(path)
os.chdir(path)
filename = 'list.txt'
dic = []
with open(filename , 'r') as f:
    dic = f.readlines()

ss = r'(\d{3})\.MID\s([\w\.\,\(\)\-\'\&\/\?\s\"]+)\s([\w\.\-]+)\s'
match = re.compile(ss)

cout = 1

for item in dic:
    mid = re.match(ss,item)
    if mid:
        number = mid.group(1)
        music = mid.group(2)
        name = mid.group(3)
        #os.rename('sjfd','sd')
        if os.path.exists(number+CON):
            #try:
                print (number + CON,name + ' - ' + music + CON)
            #except WindowsError as e:
                print os.getcwd() + '     program quit by error    tried %d times'%cout
                cout +=1
