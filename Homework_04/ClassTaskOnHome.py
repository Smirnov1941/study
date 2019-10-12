class room():
    def __init__(self, l, s, h):
        self.l = l
        self.s = s
        self.h = h
        self.S = 2*(self.l+self.s)*self.h
    def testwindow(self,a):
      if a.h+a.h2>self.h or a.s>self.s or a.s>self.l or self.S<a.h*a.s:
         print("Такой комнаты не существует")
         return 0
    def testdoor(self,a):
      if a.h>self.h or a.s>self.s or a.s>self.l or self.S<a.h*a.s:
         print("Такой комнаты не существует")
         return 0
    def appdoor(self, a):
        if a.t==1:
          self.S=self.S-a.h*a.s
    def appwindow(self, a):
       self.S=self.S-a.h*a.s
    
           

class door():
    def __init__(self, h, s, t):
        self.h = h
        self.s = s
        self.t = t


class window():
    def __init__(self, h, s, h2):
        self.h = h
        self.s = s
        self.h2 = h2


def f():
    lr = int(input())
    sr = int(input())
    hr = int(input())
    a = room(lr, sr, hr)
    S1 = 0
    q = int(input())
    i = 0
    while i < q:
        h = int(input())
        s = int(input())
        t = int(input())
        if a.testdoor(door(h,s,t))==0:
          return
        a.appdoor(door(h,s,t))
        i = i + 1
    q1 = int(input())
    i = 0
    while i < q1:
        h = int(input())
        s = int(input())
        h2 = int(input())
        w = window(h,s,h2)
        if a.testwindow(w)==0:
          return
        a.appwindow(w)
        S1=S1+w.h*w.s
        i=i+1
    print("Площадь обоев:",a.S)
    print("Коэффициент освещенноси",S1/(a.s*a.l)


f()
