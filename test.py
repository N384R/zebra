import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

# Create some data
data = pd.DataFrame({
    'x': np.random.rand(100),
    'y': np.random.rand(100),
    'z': np.random.rand(100),
    'color': np.random.rand(100)
})

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a function that will do the plotting, where the frame is the current frame
def animate(frame):
    ax.clear()
    ax.scatter(data['x'], data['y'], data['z'], c=data['color'], s=100)
    ax.view_init(30, 3*frame)

# Create an animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=100)

plt.show()
'''
When I run this code, I get the following error:
hello
'''