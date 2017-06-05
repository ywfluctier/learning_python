# -*- coding: utf-8 -*-

import codecs
with codecs.open('sans amour.txt','w','utf-8') as f:
  f.write(u'我为你付出的青春\n')
  f.write(u'这么多年\n')
  f.write(u'换来了一句谢谢你的成全\n')
  f.write(u'成全了你的潇洒与冒险\n')
  f.write(u'成全了你的碧海蓝天\n')
  
with codecs.open('sans amour.txt','r','utf-8') as f:
  for line in f.readlines():
    print line
