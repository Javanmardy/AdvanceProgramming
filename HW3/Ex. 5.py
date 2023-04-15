def a(*b):
    c = dict()
    for d in b:
        for i, e in d.items():
            if c.get(i) == None:
                c[i] = list()
                c[i].append(e)
            else:
                c[i].append(e)
    return c


print(a({'w': 50, 'x': 100, 'y': 'Green', 'z': 400},
      {'x': 300, 'y': 'Red', 'z': 600}))
