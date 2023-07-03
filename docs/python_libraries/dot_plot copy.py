import matplotlib.pyplot as plt

# convert 0.5 cm to inches
cm_per_inch = 2.54
cm = 1
inches = cm / cm_per_inch

# determine the range of the y-axis
ymin = 0
ymax = 10

# calculate the height of the figure
height = (ymax - ymin) * inches

# create a new figure with the calculated height
fig, ax = plt.subplots(figsize=(6, height))

# plot some data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
ax.plot(x, y)

# set the limits of the y-axis
ax.set_ylim(ymin, ymax)

# show the plot
plt.show()
