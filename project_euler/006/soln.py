"""
Sum of the first n natural numbers is given by
s1 = n(n+1)/2

Sum of the first n squared natural numbers is given by
s2 = n(n+1)(2n+1)/6

Hence, the difference between the first n naturals squared and the first n squared natural numbers is

s1^2 - s2
= n^2(n+1)^2/4 - n(n+1)(2n+1)/6
= n(n + 1)( 3n(n + 1) - 2(2n+1) ) / 12
= n(n + 1)( 3n^2 - n - 2 ) / 12
= n(n + 1)(n - 1)(3n + 2) / 12
"""


def main():
    n = 100
    answer = n * (n + 1) * (n - 1) * (3 * n + 2) // 12
    print(f"n = {n}, difference = {answer}")


if __name__ == '__main__':
    main()
