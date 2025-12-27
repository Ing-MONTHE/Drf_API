import requests

endpoint = "http://httpbin.org/anything"
response = requests.get(endpoint)
print(response.text)

#HTTP REQUESTS -->HTML
#REST API HTTP -->JSON :  JavaScript Object Notation