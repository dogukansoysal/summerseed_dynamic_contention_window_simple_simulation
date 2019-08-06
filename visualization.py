import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from simulation_v2 import *

time_range = 100
sta_count = 50
iteration_count = 5
cw_min = 0
cw_max = 257
throughput = [100, 0, 0, 0]


class Result:
    def __init__(self, throughput, cw_min, cw_max, sta_count):
        self.throughput = throughput
        self.cw_min = cw_min
        self.cw_max = cw_max
        self.sta_count = sta_count


def main():
    while True:
        raw_data = []
        for cw_max_counter in range(256, cw_max):
            for cw_min_counter in range(cw_min, 255):
                # total_throughput = 0
                for i in range(1, sta_count + 1):
                    temp = 0
                    for j in range(iteration_count):
                        temp += init_sim(i, cw_min_counter, cw_max_counter, throughput, time_range)

                    raw_data.append(Result(temp/iteration_count, cw_min_counter, cw_max_counter, i))
                    # total_throughput += temp/iteration_count
                # result.append(Result(total_throughput, cw_min_counter, cw_max_counter))
                print(cw_min_counter)

        result = []
        for i in range(sta_count):
            temp = i
            temp_result = Result(0, 0, 0, 0)
            while temp < (cw_max - 256) * (255 - cw_min) * sta_count:
                if raw_data[temp].throughput > temp_result.throughput:
                    temp_result = raw_data[temp]
                temp += sta_count
            result.append(temp_result)
            print("STA Count:" + str(temp_result.sta_count) + " CW MIN:" + str(temp_result.cw_min) + " CW MAX:" + str(temp_result.cw_max)
                    + " | Total Throughput:" + str(temp_result.throughput))

        output = []
        for i in range(len(result)):
            output.append(result[i].throughput)

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


    # while True:
    #     output = []
    #
    #
    #     for i in range(1, sta_count + 1):
    #         temp = 0
    #         for j in range(iteration_count):
    #             temp += init_sim(i, cw_min, cw_max, throughput, time_range)
    #         output.append(temp/iteration_count)
    #
    #
    #
    #
    #
    #     df = pd.DataFrame({'xvalues': range(1, len(output) + 1), 'yvalues': output})
    #     # plot
    #     plt.plot('xvalues', 'yvalues', data=df)
    #     plt.xlabel('STA Count')
    #     plt.ylabel('Packet Transmit Count')
    #     plt.title("CW_MIN = " + str(cw_min) + " | CW_MAX = "
    #               + str(cw_max) + "\n" + str(iteration_count) + " Iterations | "
    #               + str(time_range) + " unit time")
    #     plt.show()
    #     input("Press enter for new data set.")






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
