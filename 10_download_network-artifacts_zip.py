import requests

api_key = 'asdf1234asdf1234asdf1234'

# Example:
# sample_id = 'cc3d13fe82aa07f67fee5ae8346adfa6'
sample_id = '<SAMPLE_ID>'

network_artifacts_zip_url = 'https://panacea.threatgrid.com/api/v2/samples/{}/network-artifacts.zip'.format(sample_id)

parameters = {'api_key':api_key}

response = requests.get(network_artifacts_zip_url, params=parameters)

with open('{}_network-artifacts.zip'.format(sample_id), 'wb') as fd:
    for chunk in response.iter_content(chunk_size=512):
        fd.write(chunk)
