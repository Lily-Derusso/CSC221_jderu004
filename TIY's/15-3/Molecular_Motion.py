#random walk
import matplotlib.pyplot as plt
from random_walk import RandomWalk
#keep making new random walks as long as program is running
while True:
    rw = RandomWalk(5_000)
    rw.fill_walk()
    #plot points
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9), dpi=128)
    point_numbers = range(rw.num_points)
    #colormap
    ax.plot(rw.x_values, rw.y_values, color='blue', linewidth=3)
    ax.set_aspect('equal')

    #removes axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        plt.savefig("TIY15-3_molecular_motion.png", bbox_inches = 'tight')
        break