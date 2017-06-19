import math
import re

ip = raw_input()
m = re.match(r'(\d+)\s+(\d+)',ip)
numa = int(m.group(1))
numb = int(m.group(2))
count = [0] * 9


zhishu = [ 2 ]


#produce the list of zhishu
def check(number):
	for item in zhishu:
		if number % item == 0:
			return False
	return True

for x in range(2 , numb+1):
	if check( x ):
		zhishu.append(x)


#produce the divider list of a number
def divider(number):
	list_div = []
	while number > 1:
		for item in zhishu:
			if number % item == 0:
				list_div.append(item)
				number /= item
				continue
	#print list_div
	return list_div

#produce the real divider
def p_divider(lis):
	L = len(lis)
	real_provider = {}
	for num in range( 2 ** L ):
		mid = bin(num)[2:]
		mid = mid.rjust(L , '0')
		
		production = 1
		for item in range(L):
			if mid[item] == '1':
				production *= lis[item]
		real_provider[production] = 1
	#print real_provider
	return sorted(real_provider.keys())

#calcutlate the required number assets
def cal_div(lis):
	mid = '' #generate the initial char of each divider
	for item in lis:
		mid += str(item)[0]
	for item in range(9):
		count[item] += mid.count(str(item + 1))

for num in range(numa,numb+1):
	#print 'dealing %d' %num
	cal_div(p_divider(divider(num)))
for item in count:
		print item
