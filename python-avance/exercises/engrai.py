import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


def test(azote, phosphore, potassium):
    """3 values between 0 and 1, summing to 1.

    Error is the distance between the given 3d point and the expected 3d point.
    """
    expected = 0.3, 0.2, 0.5
    return (
        1
        - (
            (azote - expected[0]) ** 2
            + (phosphore - expected[1]) ** 2
            + (potassium - expected[2]) ** 2
        )
        ** 0.5
    )


fig = plt.figure()
ax = fig.add_subplot(projection="3d")

n = 50
possibilities = []
for azote in np.linspace(0, 1, n):
    for phosphore in np.linspace(0, 1 - azote, n):
        possibilities.append((azote, phosphore, 1 - azote - phosphore))

possibilities = np.array(possibilities)
azote = possibilities[:, 0]
phosphore = possibilities[:, 1]
potassium = possibilities[:, 2]
results = test(azote, phosphore, potassium)

ax.scatter(azote, phosphore, potassium, c=results, cmap="Oranges")
ax.set_xlabel("azote")
ax.set_ylabel("phosphore")
ax.set_zlabel("potassium")
plt.show()


def fit(params):
    return -test(params[0], params[1], params[2])


res = minimize(
    fit, [0, 0, 0], tol=1e-3, bounds=[(0, 1), (0, 1), (0, 1)], options={"disp": True}
)
print(res.x)
