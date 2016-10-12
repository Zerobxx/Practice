import requests
import re

if __name__ == '__main__':
    r = requests.get('http://www.cheemoedu.com/resource/Python/')
    jpeglist = re.findall(r'/media/ebook/image/.+\.jpg', r.content)
    i = 1
    for url in jpeglist:
        r = requests.get('http://www.cheemoedu.com' + url)
        print r.url
        print r.status_code
        with open(str(i) + '.jpg', 'wb') as f:
            f.write(r.content)
        i = i + 1


