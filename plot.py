# plot.py
# create basic plots on the swedist leaf datasets

# Done as part of Advanced Data Mining Course at BITS Pilani, Pilani Campus (CG G520)
#  authors:
#           Prabhjyot Singh Sodhi
#           Shivin Srivastava

import matplotlib.pyplot as plt


def plot():

    filename = "data/SwedishLeaf_TRAIN"

    data = open(filename, 'r').read()

    line = int(raw_input("line to plot?\n"))

    # got the nth line!
    data = data.split('\n')[line - 1]

    data = data.split(',')

    leaf_no = data[0]

    data = [float(x) for x in data[1:]]

    len_graph = len(data)

    print data[1:]
    print len_graph

    from time import sleep

    sleep(3)

    plt.plot(data)
    plt.show()


if __name__ == '__main__':
    plot()
