a = int(input())
for j in range(2, a + 1):
    for i in range(2, j):
        if j % i == 0:
            break
    else:
        print(j)
