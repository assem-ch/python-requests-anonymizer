# python-requests-anonymizer
An anonymizing tool to be used for api calls.

## Requirements
- tor
- pip install -r requirements.txt

## Install
- pip install requests_anonymizer

## Usage
The torsocks proxy must be running on port 9050, start it with the command:

- `service tor start`
or
- `systemctl start tor`


You can use it as:
```python
# Doing a simple GET request:
anonymizer.get(url='https://httpbin.org/get?arg1=123&arg2=456').text

# Doing a simple POST request:
anonymizer.post(url='https://httpbin.org/post', data={'arg1':'123','arg2':'456'}).text
```



## Disclaimer!
This tool is made for test purposes.