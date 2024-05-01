import plotly.express as px
from die import Die

#create 2 d6's
die_1 = Die()
die_2 = Die()
#make rolls and store results in list
results = []
for roll_num in range(1_000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

#analize results
frequencies = []
max_results = die_1.num_sides * die_2.num_sides
poss_results = range(1, max_results+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
#graph results
title = "Results of Rolling 3 d6 1,000 Times"
labels = {'x': 'Results', 'y': 'Frequency of Results'}
fig = px.bar(x=poss_results, y=frequencies, title = title, labels = labels)
#customize chart
fig.update_layout(xaxis_dtick=1)

fig.show()