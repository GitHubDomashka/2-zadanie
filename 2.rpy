import math
 
e=int(input("Введите диапазон"))
w=float(input("Введите шаг"))

def F(x):
 return math.sqrt(2+3*x)+72*x+math.tan(4*x+31)
 
for i in range(e):
   x=i*w
   print("{:.2f} {:.4f}".format(x,F(x)))
print("\n\n")
 
i=0
while i<e:
   x=i*w
   print("{:.2f} {:.4f}".format(x,F(x)))
   i+=1
