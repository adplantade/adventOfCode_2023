import re
with open("input.txt") as f:
 t=0
 for l in f.readlines():
  c=re.findall("\d",l)
  t+=int(c[0]+c[-1])
 print(t)