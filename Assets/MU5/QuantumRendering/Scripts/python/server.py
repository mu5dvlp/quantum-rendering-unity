import numpy as np 
import socket
import cv2

from common_logic import *
from common_quantum import *
import simulator

# //＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
SHOT_COUNT = 20000

# //ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
class UDPClient:
    def __init__(self,host='0.0.0.0',port_inbound=8888,port_outbound=8889):
        self.host = host
        self.port_inbound = port_inbound
        self.port_outbound = port_outbound
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.socket.bind((self.host,self.port_inbound))
        self.provider = simulator.Provider(SHOT_COUNT)
        self.running = True
        self.use_blur = False
        self.theta = 0


    def start(self):
        provider = self.provider
        while self.running:
            print("//〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜")
            print("Waiting for receive...")
            self.image = self.receive_image()
            print("Data received!")

            if self.image is not None:
                provider.set_image(self.image)
                provider.append_rxBlur(self.theta)
                provider.appned_measure()
                result = provider.execute_backend()
                img_proceeded = provider.convert_count_to_image(result.get_counts())
                self.broadcast_image(np.array(img_proceeded))

    
    def set_use_blur(self,cond):
        self.use_blur = cond


    def stop(self):
        self.running = False
        self.socket.close()


    def receive_image(self):
        data, addr = self.socket.recvfrom(65536)
        nparr = np.frombuffer(data, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return image


    def broadcast_image(self,image):
        _, img_encoded = cv2.imencode('.jpg', image)
        img_bytes = img_encoded.tobytes()
        self.socket.sendto(img_bytes, (self.host, self.port_outbound))
