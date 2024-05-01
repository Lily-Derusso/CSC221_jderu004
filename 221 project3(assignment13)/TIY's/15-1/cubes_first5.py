import matplotlib.pyplot as plt
#cubes
x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
#use words
ax.plot(x_values, y_values,color='green', linewidth=3)

#label title and axis
ax.set_title("Cubed Numbers 1 to 5", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
#size of tick labels
ax.tick_params(labelsize=14)
#ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')

plt.savefig("TIY15-1-firs_5_cubes.png", bbox_inches = 'tight')
plt.show()