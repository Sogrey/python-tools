# gif和matplotlib的结合

import random
from matplotlib import pyplot as plt
import gif

x = [random.randint(0, 100) for _ in range(100)]
y = [random.randint(0, 100) for _ in range(100)]

gif.options.matplotlib["dpi"] = 300

@gif.frame
def plot(i):
    xi = x[i*10:(i+1)*10]
    yi = y[i*10:(i+1)*10]
    plt.scatter(xi, yi)
    plt.xlim((0, 100))
    plt.ylim((0, 100))

frames = []
for i in range(10):
    frame = plot(i)
    frames.append(frame)

gif.save(frames, 'gif-matplotlib.gif', duration=3.5, unit="s", between="startend")