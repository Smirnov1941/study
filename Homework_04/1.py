class room():
    def __init__(self,l,s,h):
        self.l=l
        self.s=s
        self.h=h
class door():
    def __init__(self,h,s,t):
        self.h=h
        self.s=s
        self.t=t
class window():
    def __init__(self,h,s,h2):
        self.h=h
        self.s=s
        self.h2=h2
def f():
    lr=int(input())
    sr=int(input())
    hr=int(input())
    a=room(lr,sr,hr)
    q=int(input())
    i=0
    S=0
    S3=0
    L1=[]
    while i < q:
        h = int(input())
        s = int(input())
        t = int(input())
        S = S + h * s
        L1.append(door(h,s,t))
        if t==1:
            S3=S3+h*s
        i=i+1
    q1=int(input())
    i = 0
    L2 = []
    S2 = 0
    while i < q1:
        h = int(input())
        s = int(input())
        h2 = int(input())
        S2 = S2 + h * s
        L2.append(window(h, s, h2))
        i = i + 1
    if S>a.h*2*(a.s+a.l) or S2>a.h*2*(a.s+a.l):
        print("такая комната существовать не может")
    for j in range(q):
        if L1[j].h>a.h or L1[j].s>a.s:
            print("такая комната существовать не может")
            return
    for j1 in range(q1):
        if L2[j1].h+L2[j1].h2>a.h or L2[j1].s>a.s:
            print("такая комната существовать не может")
            return
    print("Площадь обоев:",a.h*2*(a.s+a.l)-S3-S2,"Коэффициент освещенности: ", S2/a.l*a.s)
f()