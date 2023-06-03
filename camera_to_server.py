import io
import cv2
import requests
import base64

def cnt_to_server(index,sensor):

    url = (f'http://180.83.19.43:7579/Mobius/HAETAE/raindrop{index}')
    
    headers =	{'Accept':'application/json',
    'X-M2M-RI':'12345',
    'X-M2M-Origin':'SpUuMHvGqsO', # change to your aei
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
        
        

def cin_to_server(index,sensor, bytes_image):

    url = (f'http://180.83.19.43:7579/Mobius/HAETAE/raindrop{index}/{sensor}')
    
    headers =	{'Accept':'application/json',
    'X-M2M-RI':'12345',
    'X-M2M-Origin':'SpUuMHvGqsO', # change to your aei
    'Content-Type':'application/vnd.onem2m-res+json; ty=4'
    }

    data =	{
        "m2m:cin": {
            "con": img_str
            }
            }

    r = requests.post(url, headers=headers, json=data)
    
    try:
        r.raise_for_status()
        print(r)
    except Exception as exc:
        print('There was a problem: %s'%(exc))
        
        

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

ret, frame = cap.read()
if not ret:
    print("프레임을 읽을 수 없습니다.")
    exit()


_, img_encoded = cv2.imencode('.jpg', frame)

image_bytes = img_encoded.tobytes()

img_str = base64.b64encode(image_bytes).decode('utf-8')


print(img_str)

cin_to_server(1,"camera",img_str)


cap.release()
