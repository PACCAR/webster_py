#### Webservice API Test Script ####
# This script submits POST requests to our ML service


import requests, json

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Step 1: Start the service!!! ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Be sure to start the webservice with:
# $ python webster_api.py



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Submit a JSON request ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Define the API endpoint
url = "http://localhost:9000/makedictionary"

# Sample data
data = json.dumps({'sl':5, 'sw':1, 'pl':3, 'pw':1})
r = requests.post(url, data)

print(r.json())
