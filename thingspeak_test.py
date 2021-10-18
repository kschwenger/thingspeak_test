# Example of GET method for adding data to a Thingspeak channel

# This code can be executed from repl.it

# Python 3 only:
from urllib.request import urlopen
from urllib.parse import urlencode

import random, time

api = "74W7TQ5E82VFO8GG"   # Enter your API key

while True:
  params = {
    "api_key":api,
    1: random.randrange(100,1000),
    2: random.randrange(100,1000),
    3: random.randrange(100,1000) }
  params = urlencode(params)   # put dict data into a GET string

  # add "?" to URL and append with parameters in GET string:
  url = "https://api.thingspeak.com/update?" + params
  try:
    response = urlopen(url)      # open the URL to send the request
    print(response.status, response.reason)  # display the response
    print(response.read()) # display response page data
    time.sleep(16)    # 15 sec minimum
  except Exception as e:
    print(e)
