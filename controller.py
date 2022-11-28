import time
import os
import subprocess

hostname = "10.0.0.76"

def ping():
    response = os.system("ping -c 4 " + hostname)

    if response == 0:
        print (hostname, 'is up!')
        return True
    else:
        print(hostname, 'is down!')
        return False


off_delay=60*1    ###for 1 minute delay 
on_delay=60*1    ###for 1 minute delay 

while True:

     if ping():
         print('host is up, calc time..')
         off_after_time=time.time()+off_delay

         while True:
             if time.time()>off_after_time:
                 print('turn off tv wifi..')
                 subprocess.call(['sh', './tplink_wifi_disable.sh']) 
                 break
     else: 
         print('host is down, calc time..')
         on_after_time=time.time()+on_delay
        
         while True:
             if time.time()>on_after_time:
                 print('turn on tv wifi..')
                 subprocess.call(['sh', './tplink_wifi_enable.sh']) 
                 print('Wait 2 mins for the host to connect...')
                 time.sleep(120)
                 break
