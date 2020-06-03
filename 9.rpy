x = int(input("Кол-во шаров "))
y = float(input("Толщина оболочки шара в метрах "))
r = float(input("Радиус внутрненного шара в метрах "))
pi=3.14
i=1
sums=0
z=0
s=0
while i <= x:
    z+=s
    s=4/3*pi*r**3
    sums += s-z
    r += y
    i += 1  


print("V =",sums,"М^3")