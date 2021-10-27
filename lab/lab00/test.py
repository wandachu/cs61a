m = max
print("type of max:", type(max))


def f2(x, y):
    global max
    print("type of max:", type(max))
    max = 5
    print("type of max:", type(max))
    m = min
    return m(x, y)


result = max(f2(3, 4), 2)
print(result)
print(type(max))
