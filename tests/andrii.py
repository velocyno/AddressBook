a ={}

b = {"1": "2", "2": "3"}

bf = frozenset(b.items())

a[bf] = "who"

print(a)