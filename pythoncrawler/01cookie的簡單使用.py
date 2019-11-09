#获取ptt八卦版的网络原始码（ｈｔｍl）
import urllib.request as req
url="https://movie.douban.com/subject/1421879/"
request=req.Request(url,headers={
    "cookie":"over18=1",#設置cookie直接訪問
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
})
with req.urlopen(request) as response:
    data =response.read().decode("utf-8")
    # print(data)
#解析原始嗎
import bs4
root =bs4.BeautifulSoup(data,"html.parser")
titles=root.find_all("li",class_="")
for title in titles:
    # print(title)
    if title.a != None: #如果li 中包含ａ標籤，打印出來
        print(title.a.string)

link=root.find("a")
print(link["href"])

