from matplotlib.animation import FuncAnimation
import numpy as np
import seaborn
import matplotlib.pyplot as plt
%matplotlib qt

y_axis= np.array(forecasted_locations['predicted_longitude'])
x_axis= np.array(forecasted_locations['predicted_latitude'])
fig = plt.figure()


ax = plt.axes(xlim=(30,50),ylim=(130,150))
plt.style.use("seaborn")
#line, = ax.plot(x_axis, y_axis, color='k') ## This line can be added to show to movement over a line chart
redDot, = plt.plot(x_axis[0], y_axis[0], 'ro')

def animate(i):
    redDot.set_data(x_axis[i],y_axis[i])
    return redDot,

ani = FuncAnimation(fig, animate, interval=500, blit=True, repeat=False)

plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title("Cell Phone tracking over 50 Time periods")
plt.show()
