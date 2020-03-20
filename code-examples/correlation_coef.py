import numpy as np
import scipy.stats
import matplotlib.pyplot as plt


X = np.array(
    [
        4,
        8,
        13,
        26,
        31,
        10,
        8,
        30,
        18,
        12,
        20,
        5,
        28,
        18,
        6,
        31,
        12,
        12,
        27,
        11,
        6,
        14,
        25,
        7,
        13,
        4,
        15,
        21,
        15,
    ]
)

y = np.array(
    [
        14,
        24,
        22,
        59,
        66,
        25,
        18,
        60,
        39,
        32,
        53,
        18,
        55,
        41,
        28,
        61,
        35,
        36,
        52,
        23,
        19,
        25,
        73,
        16,
        32,
        14,
        31,
        43,
        34,
    ]
)


def main():

    x = np.linspace(0, 40)

    a = [1, 2, 1.5, 6, 5, 2.2]
    b = [3, 3, 3, 4, 4, 4]

    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(X, y)

    plt.scatter(X, y)
    plt.plot(x, intercept + slope * x, "r", label="fitted line")
    print(r_value, r_value ** 2)
    plt.show()


main()
