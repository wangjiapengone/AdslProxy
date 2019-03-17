import os
import time


while True:
    os.system('systemctl restart tinyproxy.service')
    time.sleep(300)

