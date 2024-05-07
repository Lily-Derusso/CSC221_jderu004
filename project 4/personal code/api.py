import requests
import plotly.express as px
import plotly
#Generates bar graph of number of satellites in space by 
#country according to the Indian Space Reasearch Orginazation


#make call and check response
url = 'https://isro.vercel.app/api/customer_satellites'

#headers = {"Accept": "applications/vnd.github.v3+json"}
r = requests.get(url)
print(f"Status code: {r.status_code}")
#convert response object to dictionary
response_dict = r.json()
countries = []
num = []
used = []
x, y = countries, num

repo_dicts = response_dict["customer_satellites"]


for repo_dict in repo_dicts:
    #print((repo_dict["country"]))
    countries.append(repo_dict["country"].title())
for country in countries:
    if country not in used:
        num.append(countries.count(country))
        used.append(country)


#print(countries)
#print(num)
#print(used)

title = "Number of Customer Satellites by Country According to ISRO"
labels = {'x': 'Country', 'y': 'Satellites'}
fig = px.bar(x=used, y=num, title=title, labels=labels)
plotly.offline.plot(fig)
