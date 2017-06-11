import re

reg1 = r'[\w]+(\.[\w]+)?\@[\da-zA-Z]+(\.[a-zA-Z]){1,2}'

reg = re.compile(reg1)

test = ['someone@gmail.com','bill.gates@microsoft.com','shitman@shit.shit.shit.com','shi.tshi.tshi.t@com.com']
for itm in test:
    print itm,':  ','match!' if reg.match(itm) else 'not!'
