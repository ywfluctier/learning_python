import struct

def analy(s,name='Noname'):
  if not isinstance(s,str):
    raise TypeError('Attribute is of wrong type!')
  if len(s)<30:
    raise BaseException('Data is invalid!')
  taken = s[:29]+s[29]
  m = struct.unpack('<ccIIIIIIHH',taken)
  if m[0]+m[1] == 'BM':
    print '%s is Windows BMP:' %name
    print 'size: %d * %d      colours: %d' %(m[-4],m[-3],m[-1])
  else:
    print '% is not Windows BMP' %name
    
if __name__=='__main__':
  with open('C:/Users/luc/desktop/notitile.bmp','r') as f:
    readin = f.read(30)
  analy(readin)
  
  '''
BMP格式采用小端方式存储数据，文件头的结构按顺序如下：

两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
一个4字节整数：表示位图大小；
一个4字节整数：保留位，始终为0；
一个4字节整数：实际图像的偏移量；
一个4字节整数：Header的字节数；
一个4字节整数：图像宽度；
一个4字节整数：图像高度；
一个2字节整数：始终为1；
一个2字节整数：颜色数
'''
