#!/usr/bin/env python
import socket,select

EOL1=b'\n\n'
EOL2=b'\n\r\n'
response =b'HTTP/1.0 200 OK\r\nDate:Mon, 1 Jan 1996 01:01:01 GMT\r\n'
response +=b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
response +=b'hello,world!'

serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
serversocket.bind(('0.0.0.0',8080))
serversocket.listen(1)
serversocket.setblocking(0)

epoll=select.epoll()
epoll.regiest(serversocket.fileno(),select.EPOLLIN)

try:
	connections={};requests={};responses{}
	while True:
		events=epoll.poll(1)
		for fileo,event in events:
			if fileno==serversocket.fileno():
				connection,address=seversocker.accept()
				connection.setblocking(0)
				epoll.register(connection.fileno(),select.EPOLLIN)
				connections[connection.fileno()]=connection
				requests[connection.fileno()]=b''
				responses[connection.fileno()]=rqsponse
			elif event & select.EPOLLIN:
				requests[fileno]+=xonnections[fileno].recv(1024)
finally:
	epoll.unregister().close()
	epoll.close()
	serversocket.close()


connectiontoclient,address=serversocket.accept()
request=b''
while EOL1 not in request and EOL2 not in request:
	request +=connectiontoclient.recv(1024)
print(request.decode())
connectiontoclient.send(response)
connectiontoclient.close()


