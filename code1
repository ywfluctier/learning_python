class man( object ):
  def __init__(self,name='no_name',age=-1,gender='unknowns'):
    self.name = name
    self.age = age
    self.gender = gender
  def __str__(self):
    return 'name:%s\nage:%d\ngender:%s\n' %(self.name,self.age,self.gender)
    
class grandpa(man):
  hair = True
  def __init__(self,name='grandpa_no_name',age=-1):
    super(grandpa,self).__init__(name,age)
    self.gender='Male'
  def __str__(self):
    mid = super(grandpa,self).__str__()
    return mid + 'hair:' + str( self.hair )+'\n'
    
    
class mama(grandpa):
  def __init__(self,name='mama_no_name',age=-1):
    super(mama,self).__init__(name,age)
    self.gender='Female'
  def __str__(self):
    return super(mama,self).__str__()+'concluded by mama\n'

class papa(man):
  hair = False
  def __init__(self,name='papa_no_name',age=-1):
    super(papa,self).__init__(name,age)
    self.gender='Male'
  def __str__(self):
    mid = super(papa,self).__str__()
    return mid + 'hair:'+str( self.hair ) + '\nconcluded by papa\n'

class child(papa,mama):
  pass
    
    
    
    
    
    
dama = man()
print dama
print grandpa()
print mama()
print papa()
print child()
