#### Webservice API Test Script ####
# This script submits POST requests to our ML service


import requests, json
import pandas as pd

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Step 1: Start the service!!! ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Be sure to start the webservice with:
# $ python3 webster_api.py



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Submit a JSON request ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Define the API endpoint
url = "http://localhost:9000/makedictionary"


# Sample data
data = pd.read_csv("./Data/housing_short.csv")


# JSON Serialize the dataset
data_json = data.to_json()
data_json_dump = json.dumps(data_json)

# Post request for a dictionary
r = requests.post(url, json.dumps(data_json))

#~~~~~~~~~~~~~~~~~~~~~~~~
#### Inspect results ####
#~~~~~~~~~~~~~~~~~~~~~~~~

result = r.json()
result_df = pd.DataFrame(result)
result_df.to_csv("./Dictionary.csv", na_rep="NaN")
