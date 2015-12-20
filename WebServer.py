#import socket module
from socket import *

#Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 12000
serverConnection = ('', serverPort)

serverSocket.bind(serverConnection)
serverSocket.listen(1)

#http://localhost:12000/HelloWorld.html for testing

while True:
 #Establish the connection
 print ('Ready to serve...')
 
 connectionSocket, addr = serverSocket.accept()
 
 try:
     message = connectionSocket.recv(1024)
     filename = message.split()[1]
     f = open(filename[1:])
     outputdata = f.read()
     
     #Send the content of the requested file to the client
     for i in range(0, len(outputdata)):
         connectionSocket.send(outputdata[i].encode())
     
     connectionSocket.close()

 except IOError:
     #Send response message for file not found
     connectionSocket.send("404 Not Found".encode())
     #Close client socket
     connectionSocket.close()
serverSocket.close()
     

  
