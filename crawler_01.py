from urllib.request import urlopen
url = "https://www.baidu.com"
resp = urlopen(url)
with open("baidu.html", "w") as f:
    f.write(resp.read().decode('utf-8'))
#print(resp.read().decode('utf-8'))
print("over")

