from operator import itemgetter
import requests
import json


# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus:{r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

readable_file = './data/readable_hn_submissions.txt'
with open(readable_file, 'w') as f:
    i = 1
    for submission_dict in submission_dicts:
        f.write(f"{i}.Title: {submission_dict['title']}")
        f.write(f"\nDiscussion link: {submission_dict['hn_link']}")
        f.write(f"\nComments: {submission_dict['comments']}\n\n")
        i += 1
