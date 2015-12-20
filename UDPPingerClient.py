import socket
import time
serverName = 'localhost'
serverPort = 12000
message = "ping"
totalTime = 0.0
for i in range(0,10):
    #create a client socket to send the pings
    clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    try:
        #send the ping packet to the server and start a timer
        clientSocket.sendto(message.encode(),(serverName,serverPort))
        startTrip = time.clock()
        #set the timeout for a response to 2 seconds
        clientSocket.settimeout(2)

        #listen for a response
        response, serverAddress = clientSocket.recvfrom(1024)

        #if the server sends a response stop the timer and print the response and RTT
        endTrip = time.clock()
        roundTripTime = endTrip - startTrip
        totalTime += roundTripTime
        print("The response from the server is: " + str(response.decode()))
        print("The RTT was: " + str(roundTripTime*1000)+ " miliseconds\n")
    except socket.timeout:
        #if the timer times out, add 2 seconds the total time
        print("Request timed out\n")
        totalTime += 2
#print the total time to receive each response including timeouts
print("The total time is: " + str(totalTime*1000) + " miliseconds")
