import http.client
import json


url = 'localhost:8081'
# Create connection to the server
conn = http.client.HTTPConnection(url)

# Send Request
conn.request("GET", "/")

# GET Response
response = conn.getresponse()
response_data = response.read().decode("utf-8")

try:
    data = json.loads(response_data)
    print("Stored Data:", json.dumps(data, indent=4))
except json.JSONDecodeError:
    print("Error, Received invalid JSON response")

# Close conenction
conn.close()