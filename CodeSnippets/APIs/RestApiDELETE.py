## Simple request to DELETE information on a API URL
## Requires requests package e.g. "python -m pip install requests"

## Import requests
import requests

## Specify the API Endpoint
api_url = "https://jsonplaceholder.typicode.com/posts/1"

## No need to specify any data as you have already linked to /1 record in the api_url

## Perform a GET and store the output in response
response = requests.delete(api_url)

## Print Status Code
print(response.status_code)

## Print Headers 
#print(response.headers["Content-Type"])

# Print JSON output
#print(response.json())

## Print Text Output
#print(response.text)