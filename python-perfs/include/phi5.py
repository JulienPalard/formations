from decimal import Decimal, localcontext
from itertools import count
from functools import cache

@cache
def fib(n):
    if n in (0, 1):
        return 1
    x = n // 2
    return fib(x - 1) * fib(n - x - 1) + fib(x) * fib(n - x)

@cache
def approx_phi(n):
    return Decimal(fib(n + 1)) / Decimal(fib(n))

def approx_phi_up_to(n_digits):
    with localcontext() as ctx:
        ctx.prec = n_digits + 1
        for n in count():
            step1 = approx_phi(2 ** n)
            step2 = approx_phi(2 ** (n+1))
            if step1 == step2:
                return step1

import sys

if __name__ == "__main__":
    print(approx_phi_up_to(int(sys.argv[1])))
