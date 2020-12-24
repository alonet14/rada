import os
import scipy.signal as signal

import numpy as np

import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

cwd = os.getcwd()
print(cwd)

# get data
file_q_path = cwd + "\\resources\\rada\\Q\\Q_data.txt"

q_signal = open(file_q_path, 'r').readlines()

for index, val in enumerate(q_signal):
    q_signal[index] = float(val.replace("\n", ""))


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


fs = 100
lowcut = 0.83
highcut = 2.33

sos = signal.butter(2, 0.0466, btype='high', analog=False, output='sos', fs=100)
filtered_signal = butter_bandpass_filter(q_signal, lowcut, highcut, fs, order=3)
time_sampling = np.linspace(0, 30, 3000)

#heart signal
# plt.title("Heart Signal")
# plt.plot(time_sampling, q_signal, label="Raw Data")
# plt.plot(time_sampling, filtered_signal, label="Filted Data")
# plt.grid(True)
# plt.show()



#Breath Singal
sos2 = signal.butter(5, 0.5, btype='low', analog=False, output='sos', fs=100)
filtered_breath_signal = signal.sosfilt(sos2, q_signal)
plt.title("Breath Signal")
# plt.plot(time_sampling, q_signal, label="Raw Data")
plt.plot(time_sampling, filtered_breath_signal, label="Filted Data")
plt.show()

#Breath Singal
sos2 = signal.butter(5, 0.5, btype='low', analog=False, output='sos', fs=100)
filtered_breath_signal = signal.sosfilt(sos2, q_signal)
plt.title("Breath Signal")
# plt.plot(time_sampling, q_signal, label="Raw Data")
plt.plot(time_sampling, filtered_breath_signal, label="Filted Data")
plt.show()