from bs4 import BeautifulSoup
import requests
import sys
from keys import headers

url = "https://api.projectoxford.ai/vision/v1.0/describe"

def main():
    args = sys.argv
    route = args[1]

    soup = BeautifulSoup(open('index.html'), 'html.parser')

    for img in soup.find_all('img'):
        if 'alt' not in img:
            description = getDescription(route + img['src'])
            if description is not None:
                print description

def getDescription(src):
    res = requests.request("POST", url, headers=headers, json={"url": src})
    response = res.json()
    result = ''
    if res.status_code == requests.codes.ok and response['description']['captions'] is not None:
        for desc in response['description']['captions']:
            result += desc['text'] + '. '
        return result
    else:
        return None

if __name__ == '__main__':
    main()
