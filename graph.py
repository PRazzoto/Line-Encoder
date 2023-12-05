import matplotlib.pyplot as plt
import numpy as np


class Graph:
    def plot(list_of_lists):
        list = []
        list2 = []
        tamanho = 0
        for i in list_of_lists:
            for values in i:
                list2.append(values)
                for x in values:
                    list.append(x)
                    tamanho += 1

        t = np.arange(start=0, stop=tamanho, step=1)
        arr = np.array(list)

        for values in list2:
            plt.plot(t, arr, "-o", drawstyle="steps-mid")

        plt.xticks(np.arange(0, tamanho + 1, step=1))
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.xlim([0, tamanho])
        plt.ylim([-1, 1])
        plt.title("Gráfico")
        plt.grid(True)
        plt.figure(figsize=(10, 6))
        plt.show()
