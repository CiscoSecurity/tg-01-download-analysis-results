import requests

api_key = 'asdf1234asdf1234asdf1234'

# Example:
# artifact_sha256 = 'fbe4d4fca1a8e061e83d048d22be7031a7a01afd20f4dcef8343f92ad74570de'
artifact_sha256 = '<ARTIFACT_SHA256>'

artifact_url = 'https://panacea.threatgrid.com/api/v2/artifacts/{}/download'.format(artifact_sha256)

parameters = {'api_key':api_key}

response = requests.get(artifact_url, params=parameters)

with open('artifact-{}'.format(artifact_sha256), 'wb') as fd:
    for chunk in response.iter_content(chunk_size=512):
        fd.write(chunk)
