from src.util import file_util, get_data_util
import os
import matplotlib.pyplot as  plt
import numpy as np
# path_data_file = os.getcwd() + "\\resource\\rada\\I\\I_data.txt"
#
# get_data_util.write_data_to_file_from_nidaq(60, path_data_file, "Dev1", "ai4")

# path_i_data_file = os.getcwd() + "\\resource\\rada\\I\\I_data.txt"
path_q_data_file = os.getcwd() + "\\resource\\rada\\Q\\Q_data.txt"
print(path_q_data_file)
# list_i_data = get_data_util.read_data_from_file(path_i_data_file)
list_q_data = get_data_util.read_data_from_file(path_q_data_file)

list_haft_data
time_data = np.linspace(0,10000000, len(list_q_data))
print(list_q_data)
plt.xlabel("time")
plt.ylabel("Rada data")

plt.plot(time_data, list_q_data)
plt.show()