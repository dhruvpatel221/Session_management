import sys
import requests
import json

URL = str(sys.argv[1])
#print(URL)
re = requests.get(URL)
#print(re.json()['keys'])
lists=[]
for each in re.json()['keys']:
    value = requests.get(URL+'/'+each)
    lists.append(value.json())
print(lists)