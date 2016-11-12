from bs4 import BeautifulSoup
import requests
import sys
from keys import headers
import urllib2

url = "https://api.projectoxford.ai/vision/v1.0/describe"

def main():
    args = sys.argv
    site = args[1]
    root = args[2]

    response = requests.get(site)

    soup = BeautifulSoup(response.content, 'html.parser')

    for img in soup.find_all('img'):
        if not img.has_attr('alt'):
            link = root + img['src']
            print link
            description = getDescription(link)
            if description is not None:
                print description
            else:
                print 'Could not get description'
        elif img['alt'] == '':
            link = root + img['src']
            print link
            description = getDescription(link)
            if description is not None:
                print description
            else:
                print 'Could not get description'
        else:
            print 'alt already there'
            print img['alt']

def getDescription(src):
    res = requests.request("POST", url, headers=headers, json={"url": src})
    response = res.json()
    result = ''
    if res.status_code == requests.codes.ok and response['description']['captions'] is not None:
        for desc in response['description']['captions']:
            result += desc['text'] + '. '
        return result
    else:
        print res.text
        return None

if __name__ == '__main__':
    main()
