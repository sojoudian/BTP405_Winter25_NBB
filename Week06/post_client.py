import http.client
import json
import time
from datetime import datetime

url = 'localhost:8081'
timestamp = time.time()
dt = datetime.fromtimestamp(timestamp)

# Sample data to send (change eeach time)
payload = {"timestamp": dt.isoformat(), "message": "Hello from the Client!"}
json_payload = json.dumps(payload)

# Create connection to the server
conn = http.client.HTTPConnection(url)

# Send POST reuest
headers = {'Content-type': 'application/json'}
conn.request("POST", "/", body=json_payload, headers=headers)

# Get response
response = conn.getresponse()
response_data = response.read().decode("utf-8")

# Log response to the consle
print("Response: ", response.status, response_data)

# Close conenction
conn.close()