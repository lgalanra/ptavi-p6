#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor SIP peer2peer
"""

import socketserver
import sys


class SIPHandler(socketserver.DatagramRequestHandler):
    """
    Clase para servidor SIP p2p
    """

    def handle(self):
        """
        Método principal para manejar mensajes cliente servidor
        """
        if self.lists == []:
            self.json2registered()

        print(self.client_address)
        request = self.rfile.read().decode('utf-8')
        print(request)
        fields = request.split(' ')

        if fields[0] == 'REGISTER':
            login = fields[1].split(':')
            self.direction = login[1]
            self.dicc[self.direction] = self.client_address[0]
            aux = fields[3].split('\r')

            self.expire = int(aux[0])
            if self.expire == 0:
                del self.dicc[self.direction]

        self.register2json()
        self.wfile.write(b"SIP/2.0 200 OK " + b'\r\n\r\n')
        print(self.dicc)


if __name__ == "__main__":
    try:
        IP = sys.argv[1]
        PORT = int(sys.argv[2])
    except ValueError:
        print("Usage: python server.py IP port audio_file")
    serv = socketserver.UDPServer(('', PORT), SIPHandler)
    print("Listening...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
