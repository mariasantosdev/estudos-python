#!/usr/bin/env python3

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(("localhost", 9473))

    while True:
        msg = input("Digite aqui a sua mensagem:")

        client_socket.send(msg.encode())

except Exception as e:
    print("Erro:", e)

finally:
    client_socket.close()
