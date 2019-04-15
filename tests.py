import anonymizer
from time import time

# test GET

print(  anonymizer.get(url='https://httpbin.org/get?arg1=123&arg2=456').text )

# test POST

print(  anonymizer.post(url='https://httpbin.org/post', data={'arg1':'123','arg2':'456'}).text )

# try checking IP between 6 successive requests
t = time()
for i in range(6):
  print(anonymizer.get_ip())
print("Time taken : " + str(time() - t))
# try simultaneous requests

obj = { 'method': 'GET', 'url': "https://icanhazip.com/" }
t = time()
print([x.text for x in simultaneous_requests( [ obj, obj, obj, obj, obj, obj ] )])
print("time taken in simultaneous_requests : " + str(time() - t))
