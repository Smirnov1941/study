def f(s2,s1):
  rez=[]
  h=-100
  if len(s1)==len(s2):
    j=0
    while s2[j]>s1[j] and j<len(s2):
      j=j+1
    if j==len(s2):
      if s1[-1]>s2[-1]:
        rez.append("minus")
        a=s2
        s2=s1
        s1=a
  else:
    if len(s1)>len(s2):
      a=s2
      s2=s1
      s1=a
      rez.append("minus")
  s1=s1[::-1]
  s2=s2[::-1]
  for i in range(len(s2)):
     if i<len(s1):
       if h==i-1:
         if s2[i]-s1[i]-1>=0:
             rez.append(s2[i]-s1[i]-1)
         else :
             rez.append(s2[i]-s1[i]-1+10)
             h=i
       else:
         if s2[i]-s1[i]>=0:
             rez.append(s2[i]-s1[i])
         else :
             rez.append(s2[i]-s1[i]+10)
             h=i
     else:
       if h==i-1:
         if s2[i]-1>=0:
             rez.append(s2[i]-1)
         else :
             rez.append(s2[i]-1+10)
             h=i
       else:
          rez.append(s2[i])
  return rez[::-1]
