import requests

# URL of the Flask app running on the same EC2 instance
url = 'http://localhost:5000/generate_data'

# Data to be sent in the POST request
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Sending POST request
response = requests.post(url, json=data)

# Check if the request was successful
if response.status_code == 200:
    print("Data successfully sent!")
else:
    print("Failed to send data. Status code:", response.status_code)
