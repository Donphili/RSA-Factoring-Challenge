#!/usr/bin/python3
""" explains a method to factorize natural numbers"""
def factorization(n):
    if n % 2 == 0:
        print("{} = {} * {}".format(n, n / 2, 2))
    else:
        for i in range(3, 10):
            if n % i == 0:
                print("{} = {} * {}".format(n, i, n / i))
                break
