import grequests
TIMEOUT = 5

def get(**args):
	args['proxies'] = {'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'}
	args['timeout'] = TIMEOUT
	return grequests.map([grequests.get(**args)])[0]

def post(**args):
	args['proxies'] = {'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'}
	args['timeout'] = TIMEOUT
	return grequests.map([grequests.post(**args)])[0]

def simultaneous_requests(lst):
	# lst is an array of dicts, each dict has the key 'method' that is 'get', 'post', or any other HTTP method, url, and other parameters we might want to pass to grequests.request
	reqs = [ ]
	for req in lst:
		req['proxies']  = {'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'}
		req['timeout']  = TIMEOUT
		reqs.append( grequests.request(**req) )
	return grequests.map(reqs)

def get_ip():
	return post(url="https://icanhazip.com/").text.strip()
