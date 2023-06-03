import requests

def get_instance(index,sensor):
    url = (f'http://180.83.19.43:7579/Mobius/HAETAE/raindrop{index}/{sensor}?fu=2&la=1&ty=4&rcn=4')
    
    headers =	{'Accept':'application/json',
    'X-M2M-RI':'12345',
    'X-M2M-Origin': 'SOrigin'
    }
    
    r = requests.get(url,headers=headers)
    
    print(r)
    try:
        r.raise_for_status()
        jr=r.json()
        temp = jr['m2m:rsp']['m2m:cin']
        print(temp[0]['con'])
    except Exception as exc:
        print('Threre was a problem: %s' %(exc))
        
    
    
get_instance(3,"camera")
    

    