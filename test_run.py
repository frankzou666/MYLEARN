import requests


KERS_API_SERVER = 'http://127.0.0.1:9998/predict'
TEST_IMAGE = 'C:/programfile/curl/bin/bas.jpg'

def main():
    image = open(TEST_IMAGE,'rb')
    results={}
    values=[]
    payload = {'image': image}
    r = requests.post(KERS_API_SERVER,files = payload).json()
    if r.get('success'):
        print(r["predictions"])
        for (i, result) in enumerate(r["predictions"]):
            results[result['label']]=result['pro']
        for value in  results.values():
            values.append(value)
        maxpro = sorted(values)[len(values)-1:len(values)][0]
        for (key,value) in results.items():
            if value == maxpro:
                print(key,value)
    else:
        print('Oops, request to '+KERS_API_SERVER +' faile')


if __name__ == '__main__':
    main()