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

    INIT = METHOD + ' sip:' + LOGIN + '@' + IP + 'SIP/2.0\r\n'
    ACK = 'ACK sip: ' + LOGIN + '@' + IP + 'SIP/2.0\r\n'
    BYE = 'BYE sip: ' + LOGIN + '@' + IP + 'SIP/2.0\r\n'


    # Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
        my_socket.connect((IP, PORT))
        if sys.argv[3] == 'register':
            my_socket.send(bytes('REGISTER sip:' + sys.argv[4] +
                           ' SIP/2.0', 'utf-8') + b'\r\n' +
                           bytes('Expires: ' + str(expires_value), 'utf-8') +
                           b'\r\n\r\n')

        data = my_socket.recv(1024)
        print(data.decode('utf-8'))

        print("Socket terminado.")
