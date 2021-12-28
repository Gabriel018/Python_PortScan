import sys
import socket


def main():

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    Host =  input("Digite o Host :")
    Port =  input("Digite a porta :")

    s.connect((Host,int(Port)))
    print("Conectado")


if __name__ == '__main__':
    main()