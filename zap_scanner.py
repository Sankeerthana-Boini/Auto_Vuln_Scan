import time
from zapv2 import ZAPv2

def scan_target(target_url, api_key=''):
    zap = ZAPv2(apikey=api_key, proxies={'http': 'http://127.0.0.1:8080'})
    
    print(f'Scanning target: {target_url}')
    zap.urlopen(target_url)

    zap.spider.scan(target_url)
    while int(zap.spider.status()) < 100:
        time.sleep(1)

    zap.ascan.scan(target_url)
    while int(zap.ascan.status()) < 100:
        time.sleep(1)

    return zap.core.alerts()
