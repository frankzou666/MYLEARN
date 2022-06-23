import requests

PC_URL_TAIL='/jingtai/version.json'
H5_URL_TAIL='/static/version.json'

HOSTS=[
    {'location':'T1','type':'PC','domain':'www.vin678.com'},
    {'location':'T1','type':'H5','domain':'m.vin678.com'},
    {'location':'T2','type':'PC','domain':'www.laibalaibabumeng.com'},
    {'location':'T2','type':'H5','domain':'m.laibalaibabumeng.com'}
]

def getRequest(host):
     #处理pc请求
     if host['type'] == 'PC':
        url = 'http://' + host['domain'] + PC_URL_TAIL
        try:
           rsp = requests.get(url)
           return  rsp.json()
        except:
           return {'buildDate':None,'version': None}

     #测试h5请求
     if host['type'] == 'H5':
        url = 'http://' + host['domain'] + H5_URL_TAIL
        try:
           rsp = requests.get(url=url)
           return  rsp.json()
        except:
           return {'buildDate':None,'version': None}


def main():
    items = []
    for host in HOSTS:
        result = getRequest(host)
        host['buildDate'] = result['buildDate']
        host['version']   = result['version']
        items.append(host)

    ##先输出pc,再输出h5 ,domian字段放到最后
    for item in items:
        if item['type'] == 'PC':
           row = item['domain']
           item.pop('domain')
           item['domain'] = row
           print(item)
    for item in items:
        if item['type'] == 'H5':
            row = item['domain']
            item.pop('domain')
            item['domain'] = row
            print(item)


if __name__ == '__main__':
    main()