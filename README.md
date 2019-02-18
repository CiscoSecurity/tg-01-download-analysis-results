[![Gitter chat](https://img.shields.io/badge/gitter-join%20chat-brightgreen.svg)](https://gitter.im/CiscoSecurity/Threat-Grid "Gitter chat")

### Download Analysis Results
These scripts demonstrate how to download and save the various analysis results from Threat Grid

### Before using you must update the following:
- api_key

The scripts require either a Sample ID or SHA256 to be specified. An example with the appropriate format is provided as a comment above the variable. These variables are noted with a < (less-than-sign) and > (greater-than-sign).
- sample_id
```
# Example:
# sample_id = 'cc3d13fe82aa07f67fee5ae8346adfa6'
sample_id = '<SAMPLE_ID>'
```

- artifact_sha256
```
# Example:
# artifact_sha256 = 'fbe4d4fca1a8e061e83d048d22be7031a7a01afd20f4dcef8343f92ad74570de'
artifact_sha256 = '<ARTIFACT_SHA256>'
```

### Usage:
```
python 01_download_sample_zip.py
```

### Example script output:
The scripts will write a file to disk containing the Sample ID or SHA256 used as well as denoting what it is.
```
cc3d13fe82aa07f67fee5ae8346adfa6.zip
cc3d13fe82aa07f67fee5ae8346adfa6_analysis.json
cc3d13fe82aa07f67fee5ae8346adfa6_processes.json
artifact-fbe4d4fca1a8e061e83d048d22be7031a7a01afd20f4dcef8343f92ad74570de
```
