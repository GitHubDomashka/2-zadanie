y = int(input("Введите число:Ч "))
x = float(input("Введите число:Х "))
i=1
q=1
t=0

while i <= y:
    summa=q*x
    t += summa
    q += 1
    i += 1
    
print("Сумма y= ",t)