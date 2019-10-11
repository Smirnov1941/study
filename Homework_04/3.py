class dacha:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def S(self):
        return self.a*self.b
    def __eq__(self, other):
        return self.S()==other.S()
    def __add__(self, other):
        if self.a==other.a:
            return self(self.a,self.b+other.b)
        elif self.a==other.b:
            return self(self.a,self.b+other.a)
        elif self.b==other.b:
            return self(self.b,self.a+other.a)
        elif self.b==other.a:
            return self(self.b,self.a+other.b)
        else:
            print("Нет одинаковых сторон")
    def __sub__(self, other):
        if self.a==other.a:
            return self(self.a, abs(self.b-other.b))
        elif self.a==other.b:
            return self(self.a, abs(self.b-other.a))
        elif self.b==other.b:
            return self(self.b, abs(self.a-other.a))
        elif self.b==other.a:
            return self(self.b, abs(self.a-other.b))
        else:
            print("Нет одинаковых сторон")
