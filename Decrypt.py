import getpass
import os
#def password():

p = getpass.getpass(prompt='Enter Password ')
if p.lower() == '123456789':
    os.system("git secret reveal -p 'p' ")
else:
    print 'Incorrect Password'

