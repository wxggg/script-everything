from logging import makeLogRecord
import matplotlib.pyplot as plt


def plot_label(vals_array, label):
    x = range(len(vals_array[0]))

    for vals in vals_array:
        plt.plot(x, vals, label=label, marker='o')

    plt.xticks(x)
    plt.title(label)
    plt.legend()
    plt.show()


def plot_sub(vals_array1, vals_array2, label1, label2):
    x = range(len(vals_array1[0]))

    plt.subplot(211)
    for vals in vals_array1:
        plt.plot(x, vals, label=label1, marker='o')

    plt.xticks(x);
    plt.title(label1)
    plt.legend

    plt.subplot(212)
    for vals in vals_array2:
        plt.plot(x, vals, label=label2, marker='.')

    plt.xticks(x);
    plt.title(label2)
    plt.legend

    plt.show()


arr1 = [[1, 3, 5, 9],
        [2, 5, 3, 9],
        [1, 2, 3, 4]]

plot_label(arr1, 'test1')

plot_sub(arr1[0:2], arr1[2:3], 'test1', 'test2')
