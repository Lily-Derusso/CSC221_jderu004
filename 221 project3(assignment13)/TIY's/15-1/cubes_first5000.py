import matplotlib.pyplot as plt
#cubes
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
#use words
ax.plot(x_values, y_values,color='blue', linewidth=3)

#label title and axis
ax.set_title("Cubed Numbers 1 to 5000", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
#size of tick labels
ax.tick_params(labelsize=14)
ax.axis([0, 5500, 0, 140_000_000_000])
ax.ticklabel_format(style='plain')

plt.savefig("TIY15-1-first_5000_cubes.png", bbox_inches = 'tight')
plt.show()