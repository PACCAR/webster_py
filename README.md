# webster_py
## Python data dictionary builder and consumer.

This is a port of the websteR R package for creating and consuming data dictionaries for data science projects.

The webster_py implementation is focused on webservice deployments, with a Flask webservice interface. Datasets and dictionaries are passed in a JSON format.

# Docker Implementation Sample
A Dockerfile is added which requires <code>package-requirements</code> to be named <code>requirements.txt</code>
This is a very insecure prototype, ideally this would be run behind a reverse application proxy such as nginx.

To Build:

<code> docker build -t mltest .</code>

*If running behind a corporate firewall use **--build-arg** to pass a proxy in:*

<code> docker build -t mltest --build-arg https_proxy=itdrenlpp16059.na.paccar.com:3128 .</code>


The docker file exposes the flask app on port 5000. The following example maps that to 9000 and loads the API:

<code>
 docker run -p 9000:5000 -e FLASK_APP='webster_api.py' mltest python -m flask run --host=0.0.0.0
 </code>
