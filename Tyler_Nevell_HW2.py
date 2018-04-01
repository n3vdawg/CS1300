# -*- coding: utf-8 -*-
def calc():

    n = input("Enter first number: ")
    f = input("Enter second number: ")
    print()
    n_flt = float(n)
    f_flt = float(f)

    print(n_flt, "+", f_flt, "=", n_flt + f_flt)
    print(n_flt, "-", f_flt, "=", n_flt - f_flt)
    print(n_flt, "*", f_flt, "=", n_flt * f_flt)
    print(n_flt, "/", f_flt, "=", n_flt / f_flt)
    print(n_flt, "**", f_flt, "=", n_flt ** f_flt)

calc()