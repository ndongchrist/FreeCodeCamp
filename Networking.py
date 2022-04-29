import socket
mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect(('data.pr4e.org', 80)) #Creating a connection using a Socket
#for Connection to a server
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
#http is used for making the request(Asking for a document romeo.txt) 
#where data.pr4e.org is the site and romoe.txt the name of the file
#http is used for retrieving textfiles, documents, images etc using the 
#GET Command.
mySock.send(cmd)#this line of code sends the cmd accros the network established
#by the socket

#using the port 80. the server is awaiting for a command or communication that
#is being saved in a variable called Cmd.

while True:
    #Above we are making a request now we want use a loop for collecting 
    #the answer
    data = mySock.recv(512)#We gonna use 256bits
    if len(data)<1:#if the data contains no character we break the loop
        break
    #else we decode the data and print it
    print(data.decode())
    print(data)
mySock.close()#Close the connection