# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 08:49:24 2023

@author: laurin
"""

import sys

def FFT(n, coeffs, z, M):
    if n == 1:
        return [coeffs[0]]
    y = [0]*n
    even_coeffs = coeffs[::2]
    odd_coeffs = coeffs[1::2]
    y_even = FFT(int(n/2), even_coeffs, z**2 % M, M)
    y_odd = FFT(int(n/2), odd_coeffs, z**2 % M, M)
    x = 1
    for k in range(int(n/2)):
        y[k] = (y_even[k] + x*y_odd[k]) % M
        y[int(n/2)+k] = (y_even[k] - x*y_odd[k]) % M
        x = (z*x) % M
    return y

if __name__ == '__main__':
    (n,M,z) = sys.stdin.readline().split()
    coeffs = [0]*int(n)
    for i in range(int(n)):
        coeffs[i] = int(sys.stdin.readline())
    y = FFT(int(n), coeffs, int(z), int(M))
    for j in range(int(n)):
        sys.stdout.write(str(y[j]))
        if j != int(n)-1:
            sys.stdout.write("\n")
    