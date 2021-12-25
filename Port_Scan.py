
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

cod = client.connect_ex(("github.com", 80))

if cod == 0:
    print("Porta aberta")
else:
    print("Porta fechada")