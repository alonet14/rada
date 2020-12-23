import nidaqmx
from nidaqmx import Task

# with nidaqmx.Task() as task:
#     task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
#     print(task.read())

sample_rate = 100
task = Task()
task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
# task.timing.cfg_samp_clk_timing(sample_rate, )
print(task.timing.samp_clk_rate)
task.close()
