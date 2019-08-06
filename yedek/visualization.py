import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from simulation import *

sta_count = 100
iteration_count = 10

cw_min = 64
cw_max = 64
throughput = [100, 0, 0, 0]


def main():
    while True:
        values = []
        for i in range(sta_count):
            temp = 0
            for j in range(iteration_count):
                temp += init_sim(i, cw_min, cw_max, throughput)
            values.append(temp/iteration_count)

        df = pd.DataFrame({'xvalues': range(len(values)), 'yvalues': values})

        # plot
        line1 = plt.plot('xvalues', 'yvalues', data=df)
        plt.xlabel('STA Count')
        plt.ylabel('Time (Unit Time)')
        plt.title("CW_MIN = " + str(cw_min) + " | CW_MAX = " + str(cw_max) + "\n" + str(iteration_count) + " Iterations")
        plt.show()
        input("Press enter for new data set.")

main()
