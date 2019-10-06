def f(s1,s2):
  h=-2
  rez=[]
  s1=s1[::-1]
  s2=s2[::-1]
  for i in range(min(len(s1),len(s2))):
      if h==i-1:
          if s1[i]+s2[i]+1<10:
            rez.append(s1[i]+s2[i]+1)
          else:
            rez.append(s1[i]+s2[i]+1-10)
            h=i
      else:
          if s1[i]+s2[i]<10:
            rez.append(s1[i]+s2[i])
          else:
            rez.append(s1[i]+s2[i]-10)
            h=i
  if len(s1)>len(s2):
      for i in range(min(len(s1),len(s2)),len(s1)):
        if h==min(len(s1),len(s2))-1 or h==i-1:
          if s1[i]+1<10:
              rez.append(s1[i]+1)
          else:
              rez.append(s1[i]+1-10)
              h=i
        else:
            if s1[i]<10:
              rez.append(s1[i])
            else:
              rez.append(s1[i]-10)
              h=i
  elif len(s2)>len(s1):
      for i in range(min(len(s1),len(s2)),len(s2)):
        if h==min(len(s1),len(s2))-1 or h==i-1:
          if s2[i]+1<10:
              rez.append(s2[i]+1)
          else:
              rez.append(s2[i]+1-10)
              h=i
        else:
            if s2[i]<10:
              rez.append(s2[i])
            else:
              rez.append(s2[i]-10)
              h=i
  if h==max(len(s1),len(s2))-1:
    rez.append(1)
  return rez[::-1]
