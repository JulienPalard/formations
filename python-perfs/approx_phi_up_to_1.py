from decimal import Decimal, localcontext
from itertools import count

def fib(n):
    if n < 2: return 1
    return fib(n - 1) + fib(n - 2)

def approx_phi(n):
    return Decimal(fib(n + 1)) / Decimal(fib(n))

def approx_phi_up_to(n_digits):
    with localcontext() as ctx:
        ctx.prec = n_digits + 1
        for n in count():
            if approx_phi(n) == approx_phi(n + 1):
                return approx_phi(n)
