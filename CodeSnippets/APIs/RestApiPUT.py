## Simple request to PUT (replace) information on a API URL
## Requires requests package e.g. "python -m pip install requests"

## Import requests
import requests

## Specify the API Endpoint
api_url = "https://jsonplaceholder.typicode.com/posts/1"

## Specify the data to PUT
post = {"userId": 99, "id": 99, "title": "Test Title", "body": "Test Body"}

## Perform a GET and store the output in response
response = requests.put(api_url, json=post)

## Print Status Code
#print(response.status_code)

## Print Headers 
#print(response.headers["Content-Type"])

# Print JSON output
print(response.json())

## Print Text Output
#print(response.text)