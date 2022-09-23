def find_sum1(n, l):
    """Gros nombre non trouvé : pour 10**4 elements : 10s
    Petit nombre non trouvé : pour 10**4 elements : 10s
    """
    for i in range(len(l)):
        for j in range(len(l)):
            if i == j:
                continue
            if l[i] + l[j] == n:
                return True
    return False


def find_sum2(n, l):
    """Gros nombre non trouvé : pour 10**4 elements : 12s
    Petit nombre non trouvé : 0s
    """

    for i in range(len(l)):
        if l[i] > n:
            continue
        for j in range(len(l)):
            if i == j:
                continue
            if l[j] > n:
                continue
            if l[i] + l[j] == n:
                return True
    return False


def find_sum3(n, l):
    """Gros nombre non trouvé : pour 10**4 elements : 8s
    Petit nombre non trouvé : pour 10**4 elements : 0s
    """
    for i in range(len(l)):
        if l[i] > n:
            return False
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == n:
                return True
            if l[i] + l[j] > n:
                break
    return False


def find_sum3(n, l):
    """Gros nombre non trouvé : pour 10**4 elements : 8s
    Petit nombre non trouvé : pour 10**4 elements : 0s
    """
    for i in range(len(l)):
        if l[i] > n:
            return False
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == n:
                return True
            if l[i] + l[j] > n:
                break
    return False


def find_sum4(n, l):
    """Gros nombre non trouvé : pour 10**4 elements : 8s
    Petit nombre non trouvé : pour 10**4 elements : 5s
    """
    if len(l) <= 1:
        return False
    i = 0
    j = len(l) - 1
    while True:
        if l[i] + l[j] == n:
            return True
        i += 1
        if i == j or l[i] + l[j] > n:
            if l[i] + l[j] < n:
                return False
            i = 0
            j -= 1
            if j == 0:
                return False


def find_sum5(n, l):
    if len(l) <= 1:
        return False
    i = 0
    j = len(l) - 1
    while True:
        print(f"Searching at {i}+{j} ({l[i]+l[j]})")
        if l[i] + l[j] == n:
            return True
        if l[i] + l[j] > n:
            j -= 1
        if l[i] + l[j] < n:
            i += 1


find_sum5(12, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

exit(0)

find_sum4(2, [10, 10, 10])
from time import perf_counter
import matplotlib.pyplot as plt

k = 4
seed = list(range(10, 10 ** 5))
print(f"Testing small int a list of length {10 ** k}...")
to_find = seed[: 10 ** k]
begin = perf_counter()
find_sum4(2, to_find)
end = perf_counter()
print(f"Done in {end - begin}s")

print(f"Testing big int a list of length {10 ** k}...")
to_find = seed[: 10 ** k]
begin = perf_counter()
find_sum4(2 ** 32, to_find)
end = perf_counter()
print(f"Done in {end - begin}s")


assert find_sum1(2, [1, 1])
assert find_sum1(5, [1, 2, 3, 4, 5])
assert not find_sum1(5, [1, 3, 6])
assert not find_sum1(4, [2, 3, 4, 5, 6])
assert find_sum1(10, [2, 3, 5, 6, 7, 9])

assert find_sum2(2, [1, 1])
assert find_sum2(5, [1, 2, 3, 4, 5])
assert not find_sum2(5, [1, 3, 6])
assert not find_sum2(4, [2, 3, 4, 5, 6])
assert find_sum2(10, [2, 3, 5, 6, 7, 9])

assert find_sum3(2, [1, 1])
assert find_sum3(5, [1, 2, 3, 4, 5])
assert not find_sum3(5, [1, 3, 6])
assert not find_sum3(4, [2, 3, 4, 5, 6])
assert find_sum3(10, [2, 3, 5, 6, 7, 9])


assert find_sum4(2, [1, 1])
assert find_sum4(5, [1, 2, 3, 4, 5])
assert not find_sum4(5, [1, 3, 6])
assert not find_sum4(4, [2, 3, 4, 5, 6])
assert find_sum4(10, [2, 3, 5, 6, 7, 9])

assert find_sum5(2, [1, 1])
assert find_sum5(5, [1, 2, 3, 4, 5])
assert not find_sum5(5, [1, 3, 6])
assert not find_sum5(4, [2, 3, 4, 5, 6])
assert find_sum5(10, [2, 3, 5, 6, 7, 9])
