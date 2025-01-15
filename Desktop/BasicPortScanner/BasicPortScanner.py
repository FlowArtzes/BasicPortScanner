import pyfiglet
import sys
import socket 
from datetime import datetime

#using pyfiglet to make the ASSCI art of the port scanner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

#target variable  is a string in user input
target = input(str("Target IP : "))

#Banner
#print 50 _
print("_" * 50)
print("Scanning Target: " + target)
print("Scanning started at : " + str(datetime.now()))
print("_" * 50)

try:

    #Scan every port on the target ip
    for port in range(1,65535):
        #creating variable s an making it a socket
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #default timeout before skipping to next port
        socket.setdefaulttimeout(0.5)

    #Return open port

    #variable result which is the result of the socket if its 0 which is successful connection then print string Port and format with the port
    result = s.connect_ex((target,port))
    if result ==0:
        print("[*] Port {} is open".format(port))
    #Close socket and move on to the next port    
    s.close()

except KeyboardInterrupt:
    print("\n Exiting Application :")
    sys.exit()

except socket.error:
    print("\ Host not responding :")
    sys.exit()    
