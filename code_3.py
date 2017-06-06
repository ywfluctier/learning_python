import os
import sys

def search(goal):
  if not isinstance(goal,basestring):
    raise TypeError('Wrong type input!')
  current = os.path.abspath('.')
  for item in os.listdir('.'):
    if goal in item:
      print os.path.join(current,item)
  #print 'search is over'
      
      
if __name__ == '__main__':
  #search(raw_input('input a string:'))
  search(sys.argv[1])
