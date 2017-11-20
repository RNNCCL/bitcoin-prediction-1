import sys
import requests
import warnings

def get_url(url):
		raw_data = requests.get(url)
		raw_data.encoding = 'utf-8'
		if raw_data.status_code != 200:
			raw_data.raise_for_status()
			return False
		try:
			if isinstance(raw_data.text, unicode):
				warnings.warn('Object returned is of type unicode. Cannot parse to str in Python 2.')
		except NameError:
			pass
		return raw_data.json()
# begin 1420070400
# 1 day = 1420156800 - 1420070400 = 86400
file = open("prices.txt", "w")
for i in range(1420070400, 1511129957, 86400):
	afef = get_url("https://min-api.cryptocompare.com/data/pricehistorical?fsym=BTC&tsyms=EUR&ts="+str(i))
	for j in afef.values():
		if isinstance(j, unicode):
			print j.decode("utf-8")
			file.write(str(i) +"\n")
			file.write(str(j.decode("utf-8")) +"\n")
		else:
			print j
			file.write(str(i) +"\n")
			file.write(str(j) +"\n")
