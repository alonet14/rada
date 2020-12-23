import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

from nidaqmx import Task

recen_task = Task()
recen_task.ai_channels.add_ai_voltage_chan("Dev1/ai4")


# This function is called periodically from FuncAnimation
def animate(i,xs, ys):

    # Read rada data
    rada_data = recen_task.read()
    print(rada_data)
    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(rada_data)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Real Time Rada')
    plt.ylabel('Rada Amptitude')
    recen_task.close()


# Set up plot to call animate() function periodically
# ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=100)
# plt.show()


