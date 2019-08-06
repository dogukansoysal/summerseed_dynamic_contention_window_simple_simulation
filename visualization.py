import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from simulation_v2 import *

time_range = 100
sta_count = 100
iteration_count = 20
cw_min = 0
cw_max = 1023
throughput = [100, 0, 0, 0]

def main():
    while True:
        output = []
        for i in range(1, sta_count + 1):
            temp = 0
            for j in range(iteration_count):
                temp += init_sim(i, cw_min, cw_max, throughput, time_range)
            output.append(temp/iteration_count)

        df = pd.DataFrame({'xvalues': range(1, len(output) + 1), 'yvalues': output})
        # plot
        plt.plot('xvalues', 'yvalues', data=df)
        plt.xlabel('STA Count')
        plt.ylabel('Packet Transmit Count')
        plt.title("CW_MIN = " + str(cw_min) + " | CW_MAX = "
                  + str(cw_max) + "\n" + str(iteration_count) + " Iterations | "
                  + str(time_range) + " unit time")
        plt.show()
        input("Press enter for new data set.")






# def main():
#     while True:
#         values = []
#         for i in range(1, sta_count):
#             temp = 0
#             for j in range(iteration_count):
#                 temp += init_sim(i, cw_min, cw_max, throughput)
#             values.append(temp/iteration_count)
#
#         df = pd.DataFrame({'xvalues': range(len(values)), 'yvalues': values})
#
#         # plot
#         plt.plot('xvalues', 'yvalues', data=df)
#         plt.xlabel('STA Count')
#         plt.ylabel('Time (Unit Time)')
#         plt.title("CW_MIN = " + str(cw_min) + " | CW_MAX = "
#                   + str(cw_max) + "\n" + str(iteration_count) + " Iterations")
#         plt.show()
#         input("Press enter for new data set.")


main()
