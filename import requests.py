
import requests
import json
import pandas as pd

#response = requests.get('http://environment.data.gov.uk/water-quality/id/sampling-point/NE-42100157/measurements?determinandGroup=nutrients')
#response = requests.get('http://environment.data.gov.uk/water-quality/id/sampling-point?easting=383400&northing=583250&dist=100')
response = requests.get('http://environment.data.gov.uk/water-quality/id/sampling-point?area=3-35')
#print(response.content)
data = response.json()
#print(data['items'])

df = pd.DataFrame(data['items'])

print(df)