import requests

def read_client_secrets(file_path):
    client_secrets = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            client_secrets[key] = value
    return client_secrets

# Read client secrets
client_secrets = read_client_secrets('/Users/oliver/client.txt')

headers1 = {
    'content-type': 'application/x-www-form-urlencoded',
}

data = {
  'client_secret': client_secrets['client_secret'],
  'client_id': client_secrets['client_id'],
  'grant_type': 'client_credentials'
}

headers1 = {
    'content-type': 'application/x-www-form-urlencoded',
}

response = requests.post('https://auth.smaato.com/v2/auth/token/', headers=headers1, data=data)
v = response.json()
w = v['access_token']

print(w)

url_base = 'https://spx-api.smaato.com/publisherportal/api/publisher/v1/{}/publisher-settings'
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(w)}

publisher_ids = []
publisher_id_headers = []
sellertypes = []

for publisher_id, headers['x-spx-publisher-id'], sellertype in zip(publisher_ids, publisher_id_headers, sellertypes):
    url = url_base.format(publisher_id)
    response = requests.get(url, headers=headers)
    json_data = response.json()
    json_data['publisherRelationship'] = sellertype
    put_response = requests.put(url, headers=headers, json=json_data)
    print(put_response.json())
