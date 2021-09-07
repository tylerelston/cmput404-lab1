import requests
print("Requests version:", requests.__version__)

r = requests.get('https://www.google.com/')
print(r) # print status
print(r.content) # print content