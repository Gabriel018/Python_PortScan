import socket




s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


host = 'localhost'

port = 5433

msg = "Ola Servidor "


s.sendto(msg.encode(),(host,5432))


data, servidor = s.recvfrom(4096)
data = data.decode()
print("Client : " + data)