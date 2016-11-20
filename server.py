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
        text = self.rfile.read()
        info = text.decode('utf-8')
        print('Recibimos ' + info)

        if info.startswith('INVITE'):
            pass



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
