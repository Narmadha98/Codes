import socket
import sys
import time
s=socket.socket()
host=socket.gethostname()
print("Server will star on host :",host)
port=8080
s.bind((host,port))
print("\nServer done binding to host successfully")
print("\nServer is waiting")
s.listen(1)
conn,addr=s.accept()
print(addr,"connected to the server and is online..\n")
while(1):
    message=input(">>")
    message=message.encode()
    conn.send(message)
    print("Message sent..\n")
    incomin_msg=conn.recv(1024)
    incomin_msg=incomin_msg.decode()
    print("Client:",incomin_msg)
    print("")


      
    
      

      
