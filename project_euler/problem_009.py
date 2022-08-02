"""
a + b + c = 1000
a^2 + b^2 = c^2
= (1000 - a - b)^2
= 1000^2 - 2000(a + b) + a^2 + 2ab + b^2

1000^2 - 2000(a + b) + 2ab = 0
ab - 1000(a + b) = -1000^2/2
(a - 1000)(b - 1000) = 1000^2/2 = 5000000

(a - 1000)(b - 1000) = (2^5)(5^6)
"""


def main():
    for i in range(6):
        for j in range(7):
            a = 1000 - 2 ** i * 5 ** j
            b = 1000 - 2 ** (5 - i) * 5 ** (6 - j)
            c = 1000 - a - b
            if a > 0 and b > 0 and c > 0:
                print(f"a = {a}, b = {b}, c = {c}")
                print(f"abc = {a * b * c}")
                return


if __name__ == '__main__':
    main()
