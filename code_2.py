

import codecs
with codecs.open('C:/Users/Luc/Desktop/sans amour.txt','w','utf-8') as f:
  f.write("Je t'aime, ma cherie.\r")
  f.write('\r')
  f.write('Tu ne cesses jamais de te faire penser de moi.\r')
  f.write('\r')
  f.write("Je ne m'empeche pas de te voir tout de suite!\r")
  f.write('\r')
  f.write('Va chez moi!\r!!!!!!!!!!!')
  f.write('\r')
  f.write("Je t'embrasserai tres tres fort!!\r")
  f.write('\r')
  print 'created a file successfully...'
  
with open('sans amour.txt','r') as f:
  print f.read()
  
with open('C:/Users/Luc/Desktop/iloveyou.txt','r') as fg:
  print fg.read()
