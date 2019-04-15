import anonymizer

# test GET

print(  anonymizer.get(url='https://httpbin.org/get?arg1=123&arg2=456') )

# test POST

print(  anonymizer.post(url='https://httpbin.org/post', data={'arg1':'123','arg2':'456'}) )

# try checking IP between successive requests

for i in range(3):
  print(anonymizer.get_ip())

# now, change the IP manually between the requests

for i in range(3):
  print(anonymizer.get_ip())
  anonymizer.new_identity()

# try simultaneous requests

obj = { 'method': 'GET', 'url': "https://icanhazip.com/" }

print([x.text for x in simultaneous_requests( [ obj, obj, obj, obj, obj, obj ] )])
