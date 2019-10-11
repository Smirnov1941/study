import random
class var:
  name = ""
  def __init__(self,name):
    self.name=name  
  health = random.randint(100,150)
  power = random.randint(20,30)
  def ShowVar(self):
    print("Здоровье: ",self.health,"Сила: ",self.power)
  def damage(self,powatt):
    self.health=self.health-powatt
    if self.health<0:
      print(self.name,' получил ',powatt,' урона и погиб :(')
    else:
      print(self.name,' получил ',powatt,' урона, осталось здоровья:', self.health)
class guard_var(var):
  guard = random.randint(5,10)
  def damage(self,powatt):
    self.health=self.health-powatt+self.guard
    if self.health<0:
      print(self.name,' получил ',powatt-self.guard,' урона и погиб :(')
    else:
      print(self.name,' получил ',powatt-self.guard,' урона, осталось здоровья:', self.health)
class expert_var(var):
  def power_expert(self, power):
    if random.randint(1,5)==5:
      return power*2
    else:
      return power



