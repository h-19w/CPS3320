import matplotlib.pyplot as plt

def main ():

    x_cor = [0, 1, 2, 3, 4]
    y_cor = [2, 4, 6, 8, 10]

    plt.plot(x_cor, y_cor)
    plt.title("Graph")
    plt.xlabel("X-values")
    plt.ylabel("Y-values")
    plt.show()  

if __name__ == '__main__':
    main()