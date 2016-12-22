#~~~~~~~~~~~~~~~~~~~~~~~~
#### Import packages ####
#~~~~~~~~~~~~~~~~~~~~~~~~

# Python libraries
import pandas as pd
from flask import Flask, request, abort, jsonify
import json
import sys

# webster_py library
import webster_py_functions as webster


#~~~~~~~~~~~~~~~~~~~~~~~~~
#### Define Flask API ####
#~~~~~~~~~~~~~~~~~~~~~~~~~

app = Flask(__name__)

@app.route('/makedictionary', methods=['POST'])
def make_dictionary():
    # all kinds of error checking should go here
    data = request.get_json(force = True)
    print('Request received, building dictionary', file=sys.stderr)

    
    # convert our json to a pandas data frame
    df = pd.read_json(data)
    
    # generate webster dictionary
    output = webster.compile_dictionary(dataset= df)
    
    # Make JSON out of dictionary
    output = output.to_dict(orient = "record")
    output_json = json.dumps(output)

    return jsonify(output)

if __name__ == '__main__':
    app.run(port = 9000, debug = True)