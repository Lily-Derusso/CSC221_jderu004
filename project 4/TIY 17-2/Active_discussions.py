from operator import itemgetter
import requests
import json
import plotly.express as px
import plotly

# Make an API call, and store the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

#process info
submission_ids = r.json()
submission_dicts = []
comments, article_link = [], []
for submission_id in submission_ids[:5]:
    #call each
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r= requests.get(url)
    print(f"id: {submission_id}/tStatus code: {r.status_code}")
    response_dict = r.json()
    #build dict for each
    submission_dict = {
        'title': response_dict['title'],
        'kn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
            reverse=True)

for submission_dict in submission_dicts:
    #print(f"/nTitle: {submission_dict['title']}")
    #print(f"Discussion link: {submission_dict['hn_link']}")
    #print(f"Comments: {submission_dict['comments']}")
    title = submission_dict['title']
    link_url = submission_dict['kn_link']
    link = f"<a href='{link_url}'>{title}</a>"    
    article_link.append(link)
    comments.append(submission_dict['comments'])

title = "Most Active Discussions Currently on Hacker News"
labels = {'x': 'Article', 'y': 'Comments'}
fig = px.bar(x=article_link, y=comments, title=title, labels=labels)
plotly.offline.plot(fig)