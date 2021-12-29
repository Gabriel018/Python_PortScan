import socket




s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("Conexao Criada")

host = 'localhost'

port = 5432

s.bind((host,port))

msg = "Ola Cliente"

while True:
    dados ,  adress =  s.recvfrom(4096)

    if  dados:
        print("Servidor enviando msg")
        s.sendto(dados + msg.encode(),adress)


