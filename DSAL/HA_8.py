import math


def f1(n):
    return (n+1)/4


def f2(n):
    return (n+3)/4


def f3(n):
    return ((3 * n) + 1)/4


def c(n):
    return n == math.floor(n)


def f(n):
    if n == 1:
        return n

    if c(f1(n)):
        val = f(f1(n))
        if val == 1:
            print('f1', n, f1(n))
            return val

    if c(f2(n)):
        val = f(f2(n))
        if val == 1:
            print('f2', n, f2(n))
            return val

    if c(f3(n)):
        val = f(f3(n))
        if val == 1:
            print('f3', n, f3(n))
            return val

if __name__ == '__main__':
    print('57 ', f(57))
    print('513 ', f(513))
    print('557 ', f(557))
    print(f"1656889 {f(1656889)}")
