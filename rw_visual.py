import matplotlib.pyplot as plt
from random_walk import RandomWalk


while True:
    # Make a random walk.
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('seaborn-whitegrid')
    # print(plt.style.available)
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=10)
    # plt.savefig('random_walk.png')
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
