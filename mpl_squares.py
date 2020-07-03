import matplotlib.pyplot as plt
import math

x_values = range(1, 1000)
y_values = [x * x for x in x_values]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=10)
# ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

# Set the range for each axis.
# ax.axis([0, 101, 0, 10000])

# plt.savefig('C:\\Users\\username\\Desktop\\squares_plot.png')
plt.show()
