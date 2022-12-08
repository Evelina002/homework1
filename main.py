class Animal:
   amount_of_Animal = 0
   def __init__(self, height=160):
       self.height = height
       Animal.amount_of_Animal +=1
   def grow(self, height =1):
       self.height+=height
nick = Animal()
kate = Animal(height=70)
nick.grow(height=10)
print(kate.height)
print(nick.height)


class Car:
 amount_of_Car = 0

 def __init__(self, speed=160):
  self.speed = speed
  Car.amount_of_Car += 1

 def grow(self, speed=1):
  self.speed += speed


nick = Car()
kate = Car(speed=60)
nick.grow(speed=0.5)
print(kate.speed)
print(nick.speed)