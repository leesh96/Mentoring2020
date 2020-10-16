def gcd(a, b):
    mod = a % b
    while mod > 0:
        a = b
        b = mod
        mod = a % b
    return b

def lcm(a, b):
    x = a * b // gcd(a, b)
    return x

a, b = map(int, input().split())

print(gcd(a, b), lcm(a, b), sep="\n")