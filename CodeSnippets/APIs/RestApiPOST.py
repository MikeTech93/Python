## Simple request to POST information on a API URL
## Requires requests package e.g. "python -m pip install requests"

## Import requests
import requests

## Specify the API Endpoint
api_url = "https://jsonplaceholder.typicode.com/posts"

## Specify the data to POST
NewPost = {"userId": 99, "id": 99, "title": "Test Title", "body": "Test Body"}

## Perform a POST and store the output in response
response = requests.post(api_url, json=NewPost)

## Print Status Code
#print(response.status_code)

## Print Headers 
#print(response.headers["Content-Type"])

# Print JSON output
print(response.json())

## Print Text Output
#print(response.text)