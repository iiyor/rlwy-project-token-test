import os
import requests
from dotenv import load_dotenv

load_dotenv()

response = requests.post(
    "https://backboard.railway.com/graphql/v2",
    headers={
        "Project-Access-Token": f"{os.environ['RAILWAY_TOKEN']}",
        "Content-Type": "application/json",
    },
    json={
        "query": "query { projectToken { environmentId } }",
    },
)

data = response.json()
print(data)
