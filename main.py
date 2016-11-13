from bs4 import BeautifulSoup
import requests
import sys
from keys import headers
import urllib2

url = "https://api.projectoxford.ai/vision/v1.0/describe"

def main():
    args = sys.argv
    if (len(args) < 4):
        print "Not enough args"
        sys.exit(1)
    site = args[1]
    root = args[2]
    outputFileName = args[3]

    response = requests.get(site)

    soup = BeautifulSoup(response.content, 'html.parser')

    counter = 0
    for img in soup.find_all('img'):
        if not img.has_attr('alt') or img['alt'] == '':
            description = ''
            if not isWorkingUrl(img['src']):
                link = root + img['src']
                description = getDescription(link)
            else:
                description = getDescription(img['src'])
            if description is not None:
                print description
                img['alt'] = description
                counter += 1
            else:
                print 'Could not get description'
        else:
            print 'alt already there'
            print img['alt']

    if counter == 0:
        print 'There were no succesful alt creations. Boo'
    else:
        html = soup.prettify("utf-8")
        with open(outputFileName, "wb") as file:
            file.write(html)
        print "Outputted to {} with {} new alt tags".format(outputFileName, counter)

def isWorkingUrl(url):
    try:
        res = requests.get(url)
        return res.status_code == requests.codes.ok
    except requests.exceptions.RequestException as e:
        return False

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
