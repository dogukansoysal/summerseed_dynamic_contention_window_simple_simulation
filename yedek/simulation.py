import random
import matplotlib.pyplot as plt
import numpy as np

# Throughput 0:NONE , 1:LOW, 2:MEDIUM, 3:HIGH
# None = 0-0
# Low = 1-5
# MEDIUM = 6-10
# HIGH = 11-20


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
    for i in range(throughput[0]):
        sta.append(Sta(random.randint(0, 0), random.randint(0, init_cwmin), init_cwmin, init_cwmax))
    for i in range(throughput[1]):
        sta.append(Sta(random.randint(1, 5), random.randint(0, init_cwmin), init_cwmin, init_cwmax))
    for i in range(throughput[2]):
        sta.append(Sta(random.randint(6, 10), random.randint(0, init_cwmin), init_cwmin, init_cwmax))
    for i in range(throughput[3]):
        sta.append(Sta(random.randint(11, 20), random.randint(0, init_cwmin), init_cwmin, init_cwmax))

    #
    while len(sta) > 0:
        total_time += 1
        is_air_busy = False
        is_another_packet_in_air = False    # does more than 1 packet trying to send
        remove_list = []
        for i in range(len(sta)):
            if sta[i].cw == 0:
                if not is_air_busy:
                    is_air_busy = True
                    remove_list.append(sta[i])
                else:
                    is_another_packet_in_air = True
                    if sta[i].cwmin < sta[i].cwmax / 2:
                        sta[i].cwmin = (sta[i].cwmin + 1) * 2 - 1   # 1 fazlasinin, 2 katinin, 1 eksigi
                    sta[i].cw = random.randint(0, sta[i].cwmin)
            else:
                sta[i].cw -= 1
        if not is_another_packet_in_air:
            for i in range(len(remove_list)):
                if remove_list[i].throughput > 0:
                    remove_list[i].throughput -= 1
                else:
                    sta.remove(remove_list[i])
    return total_time
