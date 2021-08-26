def gcd (a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        while b != 0:
          h = a % b
          a = b
          b = h
        return a

if __name__ == '__main__':
     print(gcd(2, 12))