import numpy as np
import cv2
import requests
import base64


def get_instance(index,sensor):
    url = (f'http://127.0.0.1:7579/Mobius/HAETAE/raindrop{index}/{sensor}?fu=2&la=1&ty=4&rcn=4')
    
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
        return(temp[0]['con'])
    except Exception as exc:
        print('Threre was a problem: %s' %(exc))
        
    
    
img = get_instance(3,"camera")
img_bytes = base64.b64decode(img.encode('utf-8'))


nparr = np.frombuffer(img_bytes,np.uint8)
image = cv2.imdecode(nparr,cv2.IMREAD_COLOR)



cv2.imwrite('./raindrop3/result.jpg',image)
