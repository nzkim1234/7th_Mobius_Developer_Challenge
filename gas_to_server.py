import requests
import json
import RPi.GPIO as GPIO
import time
 
gas_pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(gas_pin,GPIO.IN)

def gas_detect():
     if GPIO.input(gas_pin):
          return False
     else:
          return True
     time.sleep(1)


def send_gas_value_to_server():

    url = ('http://180.83.19.43:7579/Mobius/HAETAE/gas_1')
    
    headers =	{'Accept':'application/json',
    'X-M2M-RI':'12345',
    'X-M2M-Origin':'SHAETAE', # change to your aei
    'Content-Type':'application/vnd.onem2m-res+json; ty=4'
    }

    data =	{
        "m2m:cin": {
            "con": "1"
            }
            }

    r = requests.post(url, headers=headers, json=data)
    
    try:
        r.raise_for_status()
        print(r)
    except Exception as exc:
        print('There was a problem: %s'%(exc))
        
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







if __name__ == "__main__":
    try:
        while True:
            if gas_detect():
                print("A")
                send_gas_value_to_server()
                time.sleep(1)
            else:
                print("B")
                time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
