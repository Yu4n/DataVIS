import requests
import json
from plotly.graph_objs import Bar
from plotly import offline


# Make an new API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results.
response_dict = r.json()
with open('./data/github_stars.json', 'w') as f:
    json.dump(response_dict, f, indent=4)
