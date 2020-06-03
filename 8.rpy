n = int(input('А: '))
count = 0
for i in range(100, 1000):
    summ = 0
    for j in str(i):
        summ += int(j)
    if summ == n:
        count += 1
print(count)