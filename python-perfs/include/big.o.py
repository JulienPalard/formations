import numpy as np
from scipy.special import factorial
import matplotlib.pyplot as plt


def main():
    k = 2
    x = np.arange(100)
    plt.plot(x, np.log2(x), label="O(log n)")
    plt.plot(x, x, label="O(n)")
    plt.plot(x, x * np.log2(x), label="O(n log n)")
    plt.plot(x, x ** 2, label="O(n²)")
    plt.plot(x, k ** np.array(x, dtype='float64'), label="O(cⁿ)")
    plt.plot(x, factorial(x), label="O(x!)")
    plt.legend()
    plt.ylim(0, 400)
    plt.show()


if __name__ == '__main__':
    main()
