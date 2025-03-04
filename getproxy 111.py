import requests,threading

response = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=10000&country=all&ssl=all&anonymity=all").text
with open("proxies.txt", "w+") as f:
	f.write(response)
	
def checker(proxy):
	try:
		requests.get("https://google.com",proxies={"https": "http://"+proxy},allow_redirects=True)
		with open("good.txt", "a+") as e:
			e.write(f"{proxy}\n")
		print(f"Working {proxy}")
	except:
		pass


for proxy in open("proxies.txt", "r").read().splitlines():
	threading.Thread(target=checker, args=[proxy]).start()