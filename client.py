#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente SIP que abre un socket a un servidor
"""

import socket
import sys


if __name__ == "__main__":
    # Constantes. Dirección IP del servidor y contenido a enviar
    try:
        METHOD = sys.argv[1]
        destination = str(sys.argv[2])
        LOGIN = destination[:destination.find('@')]
        IP = destination[destination.find('@')+1 : destination.find(':')]
        PORT = int(destination[destination.find(':')+1 :])
    except ValueError:
        sys.exit("Usage: client.py method receiver@IP:SIPport")

    INIT = METHOD + ' sip:' + LOGIN + '@' + IP + ' SIP/2.0\r\n'
    ACK = 'ACK sip: ' + LOGIN + '@' + IP + ' SIP/2.0\r\n'
    BYE = 'BYE sip: ' + LOGIN + '@' + IP + ' SIP/2.0\r\n'


    # Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
        my_socket.connect((IP, PORT))

        my_socket.send(bytes(INIT, 'utf-8') + b'\r\n')
        text = my_socket.recv(1024)
        info = text.decode('utf-8')

        print(info)

        if info == 'SIP/2.0 100 Trying\r\nSIP/2.0 180 Ring\r\nSIP/2.0 200 OK\r\n\r\n':
            print('Enviamos ACK')
            my_socket.send(bytes(ACK,'utf-8') + b'\r\n')
            text = my_socket.recv(1024)
            print('Enviamos BYE')
            my_socket.send(bytes(BYE,'utf-8') + b'\r\n')
            text = my_socket.recv(1024)

    print("Socket terminado.")
