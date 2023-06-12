x = 4**2020 + 2**2017 - 15
y = []
while x != 0:
    y += str(x % 2)
    x //= 2
y = y[::1]
print(y.count("1"))
