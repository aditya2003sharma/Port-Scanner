import sys
import socket
from datetime import datetime

if len(sys.argv)==2:
    target=socket.gethostbyname(sys.argv[1])
else:
    print("Syntax Error")
    print("Syntax:python3 Scanner.py <ip>")

print("*"*50)
print("Scanning Target:"+target)
print("Time Started:"+str(datetime.now()))
print("*"*50)


try:
    for port in range(50,100):#You can change the range of port according to your need,since there are 65665 ports Available
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result=s.connect_ex((target,port))
     
        if result==0:
            print(f"Port {port} is open")
        s.close()

except KeyboardInterrupt:
    print("\nExiting Program")
    sys.exit()

except socket.gaierror:
    print("Ip Address is not Resoved")
    sys.exit()
except socket.error:
    print("Could not connect to the Server")
    sys.close()