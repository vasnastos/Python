import re

x="nastosvasileios99@gmail.com"
z="wronginputjail.v"
y=re.search("^[a-zA-z][a-zA-Z0-9]*@[a-z]+\.[a-z]{2,3}",x)
k=re.search("^[a-zA-z][a-zA-Z0-9]*@[a-z]+\.[a-z]{2,3}",z)
print(y.string)
print(k)