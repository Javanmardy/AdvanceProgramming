c = 0
b = 0
for i in range(100):
    a = int(input())
    if a == b:
        c = c
    else:
        c = c + 1
    if 83 > a:
        print("too small")
    elif 83 < a:
        print("too large")
    else:
        print("It is true")
        print("number of attempts : ", c)
        break
    b = a
