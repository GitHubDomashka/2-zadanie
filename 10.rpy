a=int(input())
b=int(input())
c=int(input())
n=int(input())
count = 0
for I in range(0, int(n/a) + 1):
    for J in range(0, int(n/b) + 1):
        for N in range(0, int(n/c) + 1):
            if a*I + b*J + N*c == n:
                count = count + 1
                print(I,J,N)
print(count)
           
