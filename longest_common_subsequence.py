def lcs( str_a , str_b ):
	la = range(len( str_a ) + 1)
	lb = range(len( str_b ) + 1)
	Matrics = [[0 for i in lb] for i in la]
	pos = 0 #used to mark the last bit of the desired longest subsequence
	mlen = 0 #used to mark the largest length of the desired longest sebsequence
	for i in la[:-1]:
		for j in lb[:-1]:
			if str_a[i] == str_b[j]:
				try:
					Matrics[i + 1][j + 1] = Matrics[i][j] + 1
				except IndexError as e:
					print '%d/%d   %d/%d'%(i,len(str_a),j,len(str_b))
					for c in Matrics:
						print c
				
				if Matrics[i + 1][j + 1] > mlen:
					mlen = Matrics[i + 1][j + 1]
					pos = j + 1
	for c in Matrics:
		print c
	return str_b[pos - mlen : pos]


a = 'as12sssssssdasdsssssssssss'
b = '123456sssssssssssssssssssssssssssss0'

print 'largest subsequence between\n%s  -  %s' %(a,b)
print lcs(a,b)
