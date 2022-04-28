import socket
mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect(('data.pr4e.org', 80)) #Creating a connection using a Socket