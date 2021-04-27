import os
os.system ('git secret add 1.py 2.py && git secret hide -d ' )
os.system ('git add . ')
msg = 'Enter Commit Message: '
os.system ("git commit -m 'msg' ")
os.system ("git push -u origin master")
