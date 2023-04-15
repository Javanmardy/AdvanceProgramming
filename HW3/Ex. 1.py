def a(b):
    Max = max(b.values())
    Min = min(b.values())
    for i in b.keys():
        if b[i] == Max:
            MAX = i
        if b[i] == Min:
            MIN = i
    return MAX, MIN


print(a({'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}))
