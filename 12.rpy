import random
x=0
y=0
z=0
n=0
while 15*x+20*y+30*z<270 or 15*x+20*y+30*z>270:
    x=random.randint(0,100)
    y=random.randint(0,100)
    z=random.randint(0,100)
print("Ответ =",x,y,z)
u=15*x+20*y+30*z
print("Проверка",u)
