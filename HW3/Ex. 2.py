def a(b):
    d = list()
    for i, j in b.items():
        d.append((i, j))
    return d


print(a({'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}))
