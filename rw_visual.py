import matplotlib.pyplot as plt
from random_walk import RandomWalk


while True:
    # Make a random walk.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('seaborn-white')
    # print(plt.style.available)
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors=None, s=10)  # Ending point

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors=None, s=100)  # Starting point
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors=None, s=100)  # Ending point
    # plt.savefig('random_walk.png')

    '''
    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    '''

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
