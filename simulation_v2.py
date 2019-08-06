import random
import matplotlib.pyplot as plt
import numpy as np

# Throughput -1:NONE , 3:LOW, 2:MEDIUM, 1:HIGH


class Sta:
    def __init__(self, throughput, cw, cw_min, cw_max):
        self.throughput = throughput
        self.cw = cw
        self.packet_resend_counter = 0
        self.cw_min = cw_min
        self.cw_max = cw_max


def init_sim(sta_count, init_cw_min, init_cw_max, throughput, time_range):
    sta = []
    total_transmitted_packet = 0
    #   INIT STA    #
    for i in range(sta_count):
        sta.append(Sta(random.randint(1, 1), random.randint(0, init_cw_min), init_cw_min, init_cw_max))

    # init_cw_min = algo_1(sta_count, sta)

    while time_range > 0:
        is_air_busy = False
        is_another_packet_in_air = False  # does more than 1 packet trying to send
        sta_index_that_send_packet = None
        for i in range(len(sta)):
            if sta[i].cw == 0:
                if not is_air_busy:
                    is_air_busy = True
                    sta_index_that_send_packet = i
                else:
                    is_another_packet_in_air = True
                    if sta[i].cw_min < sta[i].cw_max / 2:
                        sta[i].cw_min = (sta[i].cw_min + 1) * 2 - 1  # 1 fazlasinin, 2 katinin, 1 eksigi
                    sta[i].cw = random.randint(0, sta[i].cw_min)
            elif sta[i].cw < 0:
                sta[i].packet_resend_counter -= 1
                if sta[i].packet_resend_counter == 0:
                    sta[i].cw = random.randint(0, sta[i].cw_min)
            else:
                sta[i].cw -= 1
        if not is_another_packet_in_air and is_air_busy:
            sta[sta_index_that_send_packet].packet_resend_counter = sta[sta_index_that_send_packet].throughput - 1
            sta[sta_index_that_send_packet].cw = -1
            if sta[sta_index_that_send_packet].packet_resend_counter == 0:
                sta[sta_index_that_send_packet].cw_min = init_cw_min
                sta[sta_index_that_send_packet].cw = random.randint(0, sta[sta_index_that_send_packet].cw_min)
            total_transmitted_packet += 1
        time_range -= 1
    return total_transmitted_packet


def algo_1(sta_count, sta):
    expected_maximum_transmitted_packet_number = sta_count

    total_package = 0
    for i in range(sta_count):
        total_package += 1 / sta[i].throughput

    average_transmitted_packet = total_package / sta_count

    if average_transmitted_packet > expected_maximum_transmitted_packet_number:
        target_cwmin = 255
        target_cwmax = 1023
    else:
        target_cwmin = int(255 * average_transmitted_packet / expected_maximum_transmitted_packet_number)
        target_cwmax = 1023

    if target_cwmin < 15:
        target_cwmin = 15

    for i in range(sta_count):
        sta[i].cwmin = target_cwmin
        sta[i].cwmax = target_cwmax

    return target_cwmin

def algo_2(sta_count, sta):
    target_cwmin = sta_count / 2
    target_cwmax = 1023

    for i in range(sta_count):
        sta[i].cwmin = target_cwmin
        sta[i].cwmax = target_cwmax

    return target_cwmin