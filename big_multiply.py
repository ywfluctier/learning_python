a = '0000000000000000000061124168406465406477509595095950020112526666666666666666666666666666666666666666662344444444444444444444444444409999999999999999923444444444444444444441555555555555551651601465445665406641066555555546041261312031021415'
b = '7894564676840668406465468406465406477509595095950068406465406477509595095950068406465406477509595095950068406465406477509595095950068406465406477509595095950068406465406477509595095950068406465406477509595095950068406465406477509595095950068406465406477509595095950068406465406477509595095950006477509568406465406477509595095950068406465406477509595095950068406465406477509595095950068406465406477509595095950068406465406477509595095950068406465406477509595095950068406465406477509595095950068406465406477509595095950068406465406477509595095950068406465406477509595095950068406465406477509595095950068406465406477509595095950068406465406477509595095950095095950046540647750959509595006888888885'
'''
actually, let the computer do the multiply jod in man's way
first of all, compute the production of each digit
then add the part of more then 9 of every produciton to its higher-digit result
repeat the procedure till the highest digit
this method can deal with the produciton of as-long-as-you-can-imagine numbers
'''
def transform( number ): #param number is actually a string. The mistake is because it was originally desgined for number multyplying
	mid = list(number) #this function is used for transforming a number into a list
	mid.reverse()
	mid = map( int , mid )
	return mid

def de_transform( list_n ):# transform a list into number-form
	list_n.reverse()
	while list_n[0] == 0:
		list_n.pop(0)
	return ''.join(map(str,list_n)) #reduce(lambda x,y: x * 10 + y , list_n)

def multiply(list_a , list_b):#do the multiplying job in man's way: digit by digit
	differ = len(list_a) - len(list_b)
	result = []
	if differ > 0:
		list_b = list_b + [0]*differ
	else:
		list_a += [0]*( -differ )
	for item in xrange(len(list_a)):
		mid = 0
		#print 'computing the %sth digit:' %item
		for ditem in xrange(item + 1):
			#print 'a[%d] *b[%d] = ' %(ditem , item - ditem)
			mid += list_a[ditem] * list_b[item - ditem]
			#print mid
		result.append( mid )
	for ditem in xrange(len(result)):
		if result[ditem] > 9:
			try:
				result[ditem + 1] += result[ditem] // 10
			except IndexError as e:
				return result
			result[ditem] %= 10
	return result
print 'computing %s * %s =' %(a,b)
print de_transform(multiply(transform(a),transform(b)))
