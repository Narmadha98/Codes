import socket
import sys
import time
s=socket.socket()
host=input(str("Please enter the host name for server"))
port=8080
s.connect((host,port))
print("Connected to chat the server")
while(1):
    incomin_msg=s.recv(1024)
    incomin_msg=incomin_msg.decode()
    print("Server:",incomin_msg)
    print("")
    message=input(">>")
    message=message.encode()
    s.send(message)
    print("Message sent..\n")


      
