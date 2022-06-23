"""
Author:
Purpose:
Date：
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt
import sympy
from scipy import integrate

sympy.init_printing()

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def main():
    """the entrance of this file"""
    t, k, T0, Ta = sympy.symbols("t, k, T_0, T_a")
    T = sympy.Function("T")
    ode = T(t).diff(t)+k*(T(t)-Ta)
    # instance of sysmp.Eq
    ode_solv = sympy.dsolve(ode)
    print(ode_solv)
    print(ode_solv.lhs)
    print(ode_solv.rhs)




if __name__ == '__main__':
    main()
