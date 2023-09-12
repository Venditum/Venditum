def kzuf(x, y, seitenlänge):
    return x // (seitenlänge // 3) + 7 - 3 * (y // (seitenlänge // 3))

print(kzuf(750, 730, 900))