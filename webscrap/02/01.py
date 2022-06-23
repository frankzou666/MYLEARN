
import requests
from urllib.parse import  quote,quote_plus

def main1():
    url = 'http://www.webscrapingfordatascience.com/paramhttp'
    url = 'http://www.webscrapingfordatascience.com/paramhttp?query=abc abc'
    url = 'http://www.webscrapingfordatascience.com/paramhttp?query='
    qs = quote_plus('abc abc')
    r = requests.get(url+qs)
    print(r.text)
    print(r.url)

def main():
    url = 'http://www.webscrapingfordatascience.com/paramhttp'
    params = {
        'query':'abc'
    }
    r = requests.get(url,params=params)
    print(r.text)
    print(r.url)

if __name__ == '__main__':
    main()