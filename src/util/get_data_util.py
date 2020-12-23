import time
import nidaqmx
from nidaqmx.system import System


def write_data_to_file_from_nidaq(amount_of_second=10, path_file="", name_device="Dev1", channel="ai0"):
    pass_time = time.time()
    list_name_device = System().devices.device_names

    if name_device in list_name_device:
        task = nidaqmx.Task()
        channel_port = name_device + "/" + channel
        task.ai_channels.add_ai_voltage_chan(channel_port)
        file = open(path_file, "w")
        while True:
            present_time = time.time()
            if present_time - pass_time > amount_of_second:
                task.close()
                file.close()
                break

            data = task.read()
            file.write(str(data) + "\n")

def read_data_from_file(path_file = ""):
    file = open(path_file, "r")
    list_data = file.readlines()
    for index, val in enumerate(list_data):
        data_ele = val.replace("\n", "")
        list_data[index] = float(data_ele)
    file.close()
    return list_data


