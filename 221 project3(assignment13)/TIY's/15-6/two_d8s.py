import plotly.express as px
from die import Die

#create 2 d8's
die_1 = Die(8)
die_2 = Die(8)
#make rolls and store results in list
results = []
for roll_num in range(1_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#analize results
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_results+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
#graph results
title = "Results of Rollinga d6 and d10 50,000 Times"
labels = {'x': 'Results', 'y': 'Frequency of Results'}
fig = px.bar(x=poss_results, y=frequencies, title = title, labels = labels)
#customize chart
fig.update_layout(xaxis_dtick=1)
#fig.show() would not work so I had to troubleshoot and 
#write to html instead
fig.write_html('TIY15-6', auto_open=True)
#fig.write_html('dice_visual_d6d10.html')