import matplotlib.pyplot as plt

def bar_graph():
    x_cor = [0, 1, 2, 3, 4]
    y_cor = [2, 4, 6, 8, 10]

    plt.bar(x_cor, y_cor, color=['blue', 'red', 'green', 'cyan', 'magenta'])
    plt.title("Bar Graph")
    plt.xlabel("X-values")
    plt.ylabel("Y-values")
    plt.show()

def main ():
    bar_graph()


if __name__ == '__main__':   
    main()
