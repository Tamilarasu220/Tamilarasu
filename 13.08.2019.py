#Files
"""
f=open("tamil.csv",'w+')
f.close()
"""
"""import csv
with open('tamil.csv','r')as i:
  data = csv.reader(i)
  for coulum in data:
        print( coulum[0])
"""
"""f=open("tamil.txt",'w')
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))
f.write(fwrite)
f.close()
f=open("tamil.txt",'r')
l=f.read()
print(l)
print(type(l))
l=f.readlines()
print(l)
print(type(l))
for ln in  f:
    print(ln)
f.close()"""
#IMPORT JSON FILE TO PYTHON
"""
import json
with open("tamil.json",'r') as f:
    details=json.load(f)
    print(details)
"""
#IMPORT DICT TO JSON

import json
with open("tamil.json") as f:
    j=json.dumps(dict.txt)
    f=write(j)
    print(f)

