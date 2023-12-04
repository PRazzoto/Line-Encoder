import matplotlib.pyplot as plt
import numpy as np
from collections import deque


class Graph:
    def plot(list_of_lists):
        list = []
        list2 = []
        for i in list_of_lists:
            for values in i:
                list2.append(values)
                for x in values:
                    list.append(x)

        for i in list:
            print(i)
        print(len(list))
        t = np.arange(len(list))

        start_index = 0
        for values in list2:
            end_index = start_index + len(values)
            normalized_values = (
                2
                * (np.array(values) - np.min(values))
                / (np.max(values) - np.min(values))
                - 1
            )
            plt.plot(t[start_index:end_index], normalized_values, drawstyle="steps-mid")
            print(t[start_index:end_index])
            start_index = end_index

        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.title("Gráfico")
        plt.grid(True)
        plt.show()
