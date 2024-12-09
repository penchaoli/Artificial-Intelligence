from urllib.request import urlopen
url = "https://www.baidu.com"
resp = urlopen(url)
print(resp.read())
print("over")

