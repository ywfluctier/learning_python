from PIL import Image
import hashlib, time

import math 

source = 'captcha.gif'  #
im = Image.open(source)

im.convert('P')
im2 = Image.new('P',im.size,255)

mid = im.histogram()
values = dict(zip(range(len(mid)),mid))
print values
print len(mid)

for x in range(im.size[0]):
	for y in range(im.size[1]):
		pix = im.getpixel((x,y))
		if pix == 220 or pix == 227:
			im2.putpixel((x,y),0)

start = -1
letters = []
for x in range(im2.size[0]):
	for y in range(im2.size[1]):
		if im2.getpixel((x,y)) != 255:
			if start >= 0:
				break
			else:
				start = x
				break
		elif y + 1 == im2.size[1] and start >= 0:
			letters.append((start,x))
			start = -1
print letters



# for i in range(im2.size[0]):
# 	print [im2.getpixel((i,j)) or '0' for j in range(im2.size[1])]
class VectorCompare:
	def magnitude(self , dic):
		summ = 0
		for k,v in dic.iteritems():
			summ += v * v
		return math.sqrt(summ)

	def relation(self, dic1 , dic2):
		mid = 0
		for k,v in dic1.iteritems():
			if dic2.has_key(k):
				mid += v * dic2[k]
		return mid / self.magnitude(dic1) / self.magnitude(dic2)
vp = VectorCompare()


def buildvector(im):
	return {i:j for i,j in enumerate(im.getdata())}


import os
store = {}
for l in '0123456789abcdefghijklmnopqrstuvwxyz':
	try:
		store[l] = [buildvector(Image.open('./iconset/%s/%s'%(l,img))) for img in os.listdir('./iconset/%s/'%l) if img != 'Thumbs.db' and img != '.DS_Store']
	except OSError:
		pass

res = ''
for letter in letters:
	im3 = im2.crop((letter[0], 0 , letter[1] , im2.size[1]))
	imv = buildvector(im3)
	glist = {}
	for guessfrom in store.keys():
		glist[guessfrom] = max(map(lambda x:vp.relation(x,imv),store[guessfrom]))
	res += sorted(glist.iteritems(),key=lambda x:x[1],reverse=True)[0][0]
print res
