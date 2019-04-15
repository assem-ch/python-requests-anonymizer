import anonymizer
from time import time

# test GET
print("Doing a simple GET request:")
print(  anonymizer.get(url='https://httpbin.org/get?arg1=123&arg2=456').text )

# test POST
print("Doing a simple POST request:")
print(  anonymizer.post(url='https://httpbin.org/post', data={'arg1':'123','arg2':'456'}).text )

# try checking IP between 6 successive requests
print("Doing 6 requests, and measuring time taken")
t = time()
for i in range(6):
  print(anonymizer.get_ip())
print("Time taken : " + str(time() - t))
# try simultaneous requests
print("Doing 6 simultaneous requests, and measuring time taken")
obj = { 'method': 'GET', 'url': "https://icanhazip.com/" }
t = time()
print([x.text for x in anonymizer.simultaneous_requests( [ obj, obj, obj, obj, obj, obj ] )])
print("time taken in simultaneous_requests : " + str(time() - t))
