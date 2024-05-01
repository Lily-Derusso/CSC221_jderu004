import matplotlib.pyplot as plt
#cubes
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
#use words
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=10)

#label title and axis
ax.set_title("Colormapped Cubed Numbers 1 to 5000", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
#size of tick labels
ax.tick_params(labelsize=14)
#ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')

plt.savefig("TIY15-2_colormapped_cubes.png", bbox_inches = 'tight')
plt.show()