import nidaqmx
from nidaqmx import Task
from nidaqmx.constants import AcquisitionType, Edge, VoltageUnits, TerminalConfiguration
import numpy as np
from nidaqmx.task import InStream
from nidaqmx.stream_readers import AnalogSingleChannelReader
import time
import matplotlib.pyplot as plt
import os
sample_rate = 100
number_sample = 10000
# init Task
task = Task()
# config Task
task.ai_channels.add_ai_voltage_chan("Dev1/ai4", terminal_config=TerminalConfiguration.RSE, min_val=-5.0, max_val=5.0,
                                     units=VoltageUnits.VOLTS)

task.timing.cfg_samp_clk_timing(sample_rate, active_edge=Edge.RISING, sample_mode=AcquisitionType.CONTINUOUS,
                                samps_per_chan=number_sample)

# getting and handling data
print("Start Reading...")
print("Start Wraping Task Into Instream...")
in_stream = InStream(task)
arr_np_data = np.empty(shape=(number_sample,), dtype=np.float64)


analogSingleChannel = AnalogSingleChannelReader(in_stream)
time.sleep(3)
pass_time = time.time()
analogSingleChannel.read_many_sample(data=arr_np_data, number_of_samples_per_channel=number_sample, timeout=110)
end_time = time.time()

print("time: {}".format(end_time - pass_time))
print("Closing Stream...")
task.close()
print("closed Stream...")

def butterwordth():
    pass

#==========write data to file==============
time_value = np.linspace(0, end_time - pass_time, number_sample)
path_data_file = os.getcwd() + "\\resources\\rada\\I\\I_data.txt"
f = open(path_data_file, "w")
for index, val in enumerate(arr_np_data):
   f.write(str(val) + "\n")
f.close()

#plot data
plt.xlabel("Time")
plt.ylabel("Rada data")
plt.plot(time_value, arr_np_data)
plt.show()

