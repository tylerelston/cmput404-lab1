import requests
print("Requests version:", requests.__version__)

r = requests.get('https://www.google.com/')
print(r) # print status
print(r.content) # print content
print()

print('Source code from github:')
r = requests.get('https://raw.githubusercontent.com/tylerelston/cmput404-lab1/main/lab1.py')
print(r.content)