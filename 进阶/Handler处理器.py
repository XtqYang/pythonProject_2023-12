import urllib.request

# 使用handler来访问百度，获取源码
url = 'http://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
}
request = urllib.request.Request(url=url, headers=headers)
# handler  build_opener  open
# 1.获取handler对象
handler = urllib.request.HTTPHandler()
# 2.获取opener对象
opener = urllib.request.build_opener(handler)
# 3.调用open方法
response = opener.open(request)
content = response.read().decode('utf-8')
print(content)
