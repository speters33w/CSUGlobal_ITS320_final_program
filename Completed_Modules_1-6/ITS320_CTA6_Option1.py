"""
For this assignment, you are given two complex numbers.
    You will print the result of their addition, subtraction, multiplication, division, and modulus operations.
    The real and imaginary precision part should be correct up to two decimal places.

Input Format
One line of input: The real and imaginary part of a number separated by a space.

Output Format
For two complex numbers and the output should be in the following sequence on separate lines:

    C + D

    C - D

    C * D

    C / D

    mod(C)

    mod(D)

For complex numbers with non-zero real and complex part, the output should be in the following format: 

A + Bi

Replace the plus symbol (+) with a minus symbol (-) when B < 0.
For complex numbers with a zero complex part, i.e. real numbers, the output should be: 

A + 0.00i

For complex numbers where the real part is zero and the complex part is non-zero, the output should be:

0.00 + Bi

references used to create this class:
# https://realpython.com/python-complex-numbers/
# https://www.udemy.com/course/math-with-python/learn/lecture/16210558
# https://byjus.com/jee/modulus-and-conjugate-of-a-complex-number/
# https://realpython.com/inheritance-composition-python/
"""
# from math import sqrt


class Complex(complex):
    pass

    def __init__(self, z):
        self.z = z

    def __str__(self):
        real = '{0:.2f}'.format(self.z.real)
        imaginary = '{0:.2f}'.format(self.z.imag)
        if self.z.imag >= 0:
            return real + '+' + imaginary + 'i'
        else:
            return real + '' + imaginary + 'i'


def main():
    Cr, Ci = [float(n) for n in input().split()]
    C = complex(Cr, Ci)
    Dr, Di = [float(n) for n in input().split()]
    D = complex(Dr, Di)
    print('')
    print(Complex(C + D))
    print(Complex(C - D))
    print(Complex(C * D))
    print(Complex(C / D))
    print(Complex(abs(C)))
    print(Complex(abs(D)))


if __name__ == '__main__':
    main()
