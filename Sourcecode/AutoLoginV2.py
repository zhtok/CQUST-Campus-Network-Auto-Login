import requests
import urllib
import re
import linecache
import time
import os
import socket

os.system("title CQUST Campust Network Auto Login v2.0")

## User configuration area start

# Campus network portal URL
url_wlanUserip = "http://aaa.cqust.edu.cn"
# Campus network get services URL
url_getService = "http://aaa.cqust.edu.cn/eportal/userV2.do?method=getServices"
# Campus network login action URL
url_startConnect = "http://aaa.cqust.edu.cn/eportal/InterFace.do?method=login"

# Import user infomation from UserInfo.txt
linecache.clearcache()
userId = linecache.getline('UserInfo.txt' , 2).strip('\n')
password = linecache.getline('UserInfo.txt' , 4).strip('\n')

# User information fixed in program
# userId = Your ID number or username here
# password = Your password here

## User configuration area end

print("Welcome to CQUST Campust Network Auto Login v2.0\n")
print("Designed by Chris")
print("E-mail:chris@cqust.edu.cn")
print("Updated at 2021/09/28 18:57\n")

print("Checking the Internet connection...")

netChinaStatus=os.system('ping www.baidu.com -n 3 -w 10')

if netChinaStatus>0:
    print("\nYou are not connected to the Internet!\n")
    print("Checking campus network connection...")
    netCampusStatus=os.system('ping aaa.cqust.edu.cn -n 3 -w 10')
    if netCampusStatus>0:
        serviceStatus=False
        print("\nYou are not in campus network service!\n")
        i=3
        for _ in range(0,3):
            print("\rProgram will exit in {} seconds...  ".format(i), end="")
            time.sleep(1)
            i -= 1         
    else:
        print("\nYou are in campus network service!\n")
        serviceStatus=True
        i=3
        for _ in range(0,3):
            print("\rProgram will start in {} seconds...  ".format(i), end="")
            time.sleep(1)
            i -= 1 
else:
    serviceStatus=False
    print("\nYou are already connected to the Internet!\n")
    i=3
    for _ in range(0,3):
        print("\rProgram will exit in {} seconds...  ".format(i), end="")
        time.sleep(1)
        i -= 1     

while serviceStatus:
    
    print("\n\nUserID:",userId)
    
    data_getService = {
        "username": userId,
        "search": ''
    }

    getService = requests.post(url_getService,data_getService).text

    service = urllib.parse.quote(getService.replace("校园内网","").replace("@","").encode('UTF-8'))

    wlanUserip = requests.get(url_wlanUserip).text.replace("<script>top.self.location.href='http://aaa.cqust.edu.cn/eportal/index.jsp?","").replace("'</script>","")

    data_startConnect = {
        "userId": userId,
        "password": password,
        "service": service,
        "queryString": wlanUserip,
        "operatorPwd": '',
        "operatorUserId": '',
        "validcode": '',
        "passwordEncrypt": "false"
    }

    print("\nConnecting to the Internet...")
    startConnect = requests.post(url_startConnect,data_startConnect)
    statusCode = startConnect.text.find('success')
    if statusCode>0:
        print("You are now connected to the Internet via campus network!\n")
        i=5
        for _ in range(0,5):
            print("\rProgram will exit in {} seconds...  ".format(i), end="")
            time.sleep(1)
            i -= 1 
            if i>0:
                serviceStatus=False
    else:
        print("Connection failed! Please make sure your ID and password are correct.\n")
        i=10
        for _ in range(0,10):
            print("\rProgram will retry to connect in {} seconds.  ".format(i), end="")
            time.sleep(1)
            i -= 1
     
exit
        
