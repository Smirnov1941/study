import random
s = [1,0,1,0,3,4,3,"Dog",1,"Dog"]
r=random.random()
for i in range(len(s)):
    if r==s[i]:
        r=random.random()
        i=0
for i in range(len(s)):
    a=i
    for i in range(a+1,len(s)):
        if s[i] == s[a] and s[i]!=r:
            s[i]=r
while r in s:
    s.remove(r)
print(s)
