import requests

# URL of the Flask app running on the same EC2 instance
url = 'http://localhost:5000/show_data'

# Sending GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Print the retrieved data
    print("Data retrieved:", response.json())
else:
    print("Failed to retrieve data. Status code:", response.status_code)
