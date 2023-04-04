b = 0
c = 1
a = int(input())
for i in range(a):
    d = b + c
    b = c
    c = d
print(d)
