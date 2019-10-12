import random

# описание классов
class var:
    name = ""

    def __init__(self, name):
       self.name = name
       self.health = random.randint(100, 150)
       self.power = random.randint(20, 30)
    def ShowVar(self):
       print(self.name, ": Здоровье: ", self.health, "Сила: ", self.power)

    def damage(self, powatt):
        self.health = self.health - powatt
        if self.health < 0:
            print(self.name, ' получил ', powatt, ' урона и погиб :(')
        else:
            print(self.name, ' получил ', powatt, ' урона, осталось здоровья:',
                  self.health)


class guard_var(var):
    guard = random.randint(5, 10)

    def damage(self, powatt):
        self.health = self.health - powatt + self.guard
        if self.health < 0:
            print(self.name, ' получил ', powatt - self.guard,
                  ' урона и погиб :(')
        else:
            print(self.name, ' получил ', powatt - self.guard,
                  ' урона, осталось здоровья:', self.health)


class expert_var(var):
    def power_expert(self):
        if random.randint(1, 5) == 5:
            return self.power * 2
        else:
            return self.power

# задание 1
a = var('a1')
a.ShowVar()
b = guard_var('b1')
b.ShowVar()
c = expert_var('c1')
c.ShowVar()

# задание 2
i=1
print("Бой a и b")
while a.health>0 and b.health>0:
  if i%2==0:
    b.damage(a.power)
  else:
    a.damage(b.power)
  i=i+1

a2 = var('a2')
a2.ShowVar()
i=1
print("Бой a2 и с")
while a2.health>0 and c.health>0:
  if i%2==0:
    c.damage(a.power)
  else:
    a2.damage(c.power_expert())
  i=i+1

b2 = guard_var('b2')
b2.ShowVar()
c2 = expert_var('c2')
c2.ShowVar()
i=1
print("Бой b2 и c2")
while b2.health>0 and c2.health>0:
  if i%2==0:
    c2.damage(b2.power)
  else:
    b2.damage(c2.power_expert())
  i=i+1

# задание 3
arm11 = var('arm11')
arm12 = var('arm12')
arm13 = var('arm13')
arm14 = var('arm14')
arm15 = guard_var('arm15')
arm16 = guard_var('arm16')
arm17 = guard_var('arm17')
arm18 = guard_var('arm18')
arm19= expert_var('arm19')
arm110= expert_var('arm110')
arm1=[arm11, arm12, arm13, arm14, arm15, arm16, arm17, arm18, arm19, arm110]

arm21 = var('arm21')
arm22 = var('arm22')
arm23 = var('arm23')
arm24 = var('arm24')
arm25 = guard_var('arm25')
arm26 = guard_var('arm26')
arm27 = guard_var('arm27')
arm28 = guard_var('arm28')
arm29= expert_var('arm29')
arm210= expert_var('arm210')
arm2=[arm21, arm22, arm23, arm24, arm25, arm26, arm27, arm28, arm29, arm210]

i=1
while len(arm1)>0 and len(arm2)>0:
  if i%2==0:
    j=random.randint(0,len(arm2)-1)
    j1=random.randint(0,len(arm1)-1)
    if type(arm2[j]) is expert_var:
      arm1[j1].damage(arm2[j].power_expert())
    else:
      arm1[j1].damage(arm2[j].power)
    if arm1[j1].health<0:
      del arm1[j1]
  else:
    j=random.randint(0,len(arm1)-1)
    j1=random.randint(0,len(arm2)-1)
    if type(arm1[j]) is expert_var:
      arm2[j1].damage(arm1[j].power_expert())
    else:
      arm2[j1].damage(arm1[j].power)
    if arm2[j1].health<0:
      del arm2[j1]
  i=i+1
if i%2==0:
  print("Победила армия1")
else:
  print("Победила армия2")
