import matplotlib.pyplot as plt
import numpy as np
import json

top = json.load(open('Special/missingTop5.json', 'r'))
bottom = json.load(open('Special/missingBottom5.json', 'r'))


xAxisT = [key for key, value in top.items()]
yAxisT = [value for key, value in top.items()]
xAxisB = [key for key, value in bottom.items()]
yAxisB = [value for key, value in bottom.items()]
plt.grid(True)

plt.bar(xAxisT, yAxisT, width = .75, color = 'red')
plt.bar(xAxisB, yAxisB, width = .75, color = 'blue')

plt.xlabel('States')
plt.ylabel('Missing persons (per 100,000)')
plt.xticks(rotation=45)
plt.title('Missing Persons as of Sep 15, 2023 by State per 100,000 People (Top and Bottom Five States)')