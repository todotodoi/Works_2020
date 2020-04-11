import urllib2
import re

for page in range(1, 31):
    url = "https://www.boannews.com/media/list.asp?Page="+ str(page) +"&mkind=1&kind="
    user_agent = "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    request = urllib2.Request(url, None, {'User-Agent':user_agent})
    data = urllib2.urlopen(request).read()
    
    result = []
    data = str(data).split('\n')


    for i in data:
        if re.search("news_txt", i):
             i =re.sub("<.*?>", "", i)
             i = re.sub("\t", "", i)
             result.append(i)
            
        if re.search("news_main_title", i):
            i =re.sub("<.*?>", "", i)
            i = re.sub("\t", "", i)
            result.append(i)

    for i in result:    
        print i
