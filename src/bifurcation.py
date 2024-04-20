import numpy as np
import time
import matplotlib.pyplot as plt

# variables you can change
res = 100000
amount = 100


def logy(itr: int, initp: float, ra: float) -> float:
    """
    Iterates the function `f(x) = ra * x * (1 - x)`

    :param itr: Amount to be iterated on
    :param initp: Initial Population (%)
    :param ra: Rate of growth (%)
    :return: The Resulting Population
    """
    p = initp
    for j in range(itr):
        p = ra * p * (1 - p)
    return p


def prevalue(ras: list[float], amt: int) -> list[float]:
    """
    Prevalues the y-values.
    It does this for optimization.
    :param ras: List of Rates
    :param amt: Amount of Iterations
    :return: List of prevalues
    """
    prvs = []
    for rt in ras:
        prvs.append(logy(amt, 0.5, rt))
    return prvs


def get_last_ys(ras: list[float], out_list: list[float], prevalues: list[float], rang: int):
    """
    Iterates the last 100 y-values and puts them in a list.
    :param rang: The amount of y-values per x-value
    :param ras: List of Rates
    :param out_list: The Output List
    :param prevalues: List of prevalues
    """
    for ind in range(len(ras)):
        stp = prevalues[ind]
        for _step in range(rang):
            out_list.append(stp)
            stp = ras[ind] * stp * (1 - stp)


# noinspection PyTypeChecker
def main():
    """
    The main function (If it somehow wasn't clear).
    """
    plt.style.use('dark_background')

    # noinspection PyTypeChecker
    rs = np.linspace(0, 4, res, dtype=float)
    print("Creating prevalues...", end="")
    ts = time.perf_counter()
    prevalues = prevalue(rs, 100)
    te = time.perf_counter()
    strg = "done ({})".format(te - ts)
    print(strg)

    sprs = []
    print("Creating spread-values...", end="")
    ts = time.perf_counter()
    for r in rs:
        for i in range(100):
            sprs.append(r)
    te = time.perf_counter()
    strg = "done ({})".format(te - ts)
    print(strg)

    fig, ax = plt.subplots()
    ax.set_title("LogisticMap")
    ax.set_xlabel('Rate')
    ax.set_ylabel('Population (%)')
    plt.ylim(0, 1)

    ys = []
    print("Creating y-values...", end="")
    ts = time.perf_counter()
    get_last_ys(rs, ys, prevalues, amount)
    te = time.perf_counter()
    strg = "done ({})".format(te - ts)
    print(strg)

    print("Creating plot...", end="")
    ts = time.perf_counter()
    ax.scatter(sprs, ys, s=0.01, color=(1, 1, 1))
    te = time.perf_counter()
    strg = "done ({})".format(te - ts)
    print(strg)

    plt.show()


main()
