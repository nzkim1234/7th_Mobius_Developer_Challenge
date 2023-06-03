import requests

def cnt_to_server(index,sensor):

    url = (f'http://180.83.19.43:7579/Mobius/HAETAE/raindrop{index}')
    
    headers =	{'Accept':'application/json',
    'X-M2M-RI':'12345',
    'X-M2M-Origin':'SHAETAE', # change to your aei
    'Content-Type':'application/vnd.onem2m-res+json; ty=3'
    }

    data =	{
        "m2m:cnt":{
            "rn": f"{sensor}"
        }
            }

    r = requests.post(url, headers=headers, json=data)
    
    try:
        r.raise_for_status()
        print(r)
    except Exception as exc:
        print('There was a problem: %s'%(exc))
        
        
cnt_to_server(3,"gas")
cnt_to_server(1,"gas")