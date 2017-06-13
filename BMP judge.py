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