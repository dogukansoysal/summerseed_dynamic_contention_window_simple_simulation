import random
import matplotlib.pyplot as plt
import numpy as np

# Throughput 0:NONE , 1:LOW, 2:MEDIUM, 3:HIGH
# None = 0-0
# Low = 1-5
# MEDIUM = 6-10
# HIGH = >11

class Sta:
    def __init__(self, throughput, cw, cwmin, cwmax):
        self.throughput = throughput
        self.cw = cw
        self.cwmin = cwmin
        self.cwmax = cwmax


def init_sim(sta_count, init_cwmin, init_cwmax, throughput):
    total_time = 0
    sta = []

    #   INIT STA    #
    for i in range(sta_count):
        sta.append(Sta(random.randint(0, 3), random.randint(0, init_cwmin), init_cwmin, init_cwmax))

    #algo_1(sta_count, sta)

    while len(sta) > 0:
        algo_1(len(sta), sta)
        total_time += 1
        is_air_busy = False
        is_another_packet_in_air = False # does more than 1 packet trying to send
        remove_list = []
        for i in range(len(sta)):
            if sta[i].cw == 0:
                if not is_air_busy:
                    is_air_busy = True
                    remove_list.append(i)
                else:
                    is_another_packet_in_air = True
                    if sta[i].cwmin < sta[i].cwmax / 2:
                        sta[i].cwmin = (sta[i].cwmin + 1) * 2 - 1 # 1 fazlasinin, 2 katinin, 1 eksigi
                    sta[i].cw = random.randint(0, sta[i].cwmin)
            else:
                sta[i].cw -= 1
        if not is_another_packet_in_air:
            for i in range(len(remove_list)):
                sta.pop(remove_list[i])
    return total_time


def algo_1(sta_count, sta):
    expected_maximum_transmitted_packet_number = 1
    total_package = sta_count
    #for i in range(sta_count):
        #total_package += sta[i].throughput

    average_transmitted_packet = total_package / sta_count

    if average_transmitted_packet > expected_maximum_transmitted_packet_number:
        target_cwmin = 255
        target_cwmax = 1023
    else:
        target_cwmin = 255 * average_transmitted_packet / expected_maximum_transmitted_packet_number
        target_cwmax = 1023

    if target_cwmin < 15:
        target_cwmin = 15

    for i in range(sta_count):
        sta[i].cwmin = target_cwmin
        sta[i].cwmax = target_cwmax
