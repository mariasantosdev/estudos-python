#!/usr/bin/env python3

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("localhost", 9473))

server_socket.listen()

print("Aguardando conexão...")

try:
    conn, addr = server_socket.accept()
    print("Conexão estabelecida com", addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("Nova mensagem do host %s: %s" % (addr, data.decode()))

except Exception as e:
    print("Erro:", e)

finally:
    server_socket.close()
