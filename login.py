import os
import hashlib

CONFIDENTIAL = 'database.db'

fp = open(CONFIDENTIAL,'a')
fp.close()
assert os.path.exists(CONFIDENTIAL)

dic = []
with open(CONFIDENTIAL, 'rb') as read_db:
    dic = read_db.readlines()

import re

standard = re.compile(r'([\da-zA-Z\_]+)[\s]*(0)[\s]*([\w]+)')
database = {}
for item in dic:
    # print item
    if standard.match(item) and len(item) > 33:
        mid_standard = standard.match(item)
        # print mid_standard.groups()
        if mid_standard.group(2) != '0':
            continue
        database[mid_standard.group(1)] = mid_standard.group(3)


# print database



def name_judge(name):
  if not isinstance(name,str):
    return 1 #wrong type input
  if re.match(r'^[\da-zA-Z\_]+$', name) == None:
    return 2 #invalid
  if name in database:
    return 4 #repeat
  if name not in database:
    return 0 #not exist

def action(act=0):
    mid_list = ['registration','login','password-update']
    error_dict = {0:'does not exist',1:'is of wrong type',2:'is invalid',4:'is occupied'}
    print 'You are conducting the action of %s!' % mid_list[act]
    username = raw_input('Please input your username:')
    while(name_judge(username)+act) in range(1,5):
      if username == '#quit':
        print 'Aborted inputting username!'
        return
      username = raw_input( 'Username %s %s! \nPlease reinput your username: (type #quit to abort)    ' %(username,error_dict[name_judge(username)]))
    password = raw_input('Please input your password:')
    if act == 0:
        register(username, password)
    elif act == 1:
        login(username, password)
    else:
      update(username,password)

def md5_encode(password,username = ''):
  create = hashlib.md5()
  create.update(password+username)
  return create.hexdigest()

def register(username, password):
    g_password = md5_encode(password,username)
    with open(CONFIDENTIAL, 'a') as secret:
        secret.write('\n%s    0    %s' % (username, g_password))
    print 'Registration success!'
    database[username] = g_password

def verifier(username, password):
    return md5_encode(password,username) == database[username]

def login(username, password):
    if verifier(username, password):
        print 'Username %s login succeeded!' % username
    else:
        print 'Wrong password input, username %s login failed!' % username

def update(username, password):
  if verifier(username,password):
    password = raw_input('Please input your new password:')
    password = md5_encode(password,username)
    database[username] = password
    with open(CONFIDENTIAL,'w+') as p_update:
      for item in database.keys():
        p_update.write('\n%s    0    %s' %(item,database[item]))
    print 'Password updated successfully!'
  else:
    print 'Wrong password input, password update failure!'


if __name__ == '__main__':
    action()