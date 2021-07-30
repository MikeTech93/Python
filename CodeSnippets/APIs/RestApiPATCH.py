## Simple request to PATCH (update) information on a API URL
## Requires requests package e.g. "python -m pip install requests"

## Import requests
import requests

## Specify the API Endpoint
api_url = "https://jsonplaceholder.typicode.com/posts/1"

## Specify the data to PUT
post = {"title": "New Test Title"}

## Perform a PATCH and update the record accordingly
response = requests.patch(api_url, json=post)

## Print Status Code
#print(response.status_code)

## Print Headers 
#print(response.headers["Content-Type"])

# Print JSON output
print(response.json())

## Print Text Output
#print(response.text)