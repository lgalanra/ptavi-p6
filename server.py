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
        print('Recibimos -> ' + info)

        if info.startswith('INVITE'):
            self.wfile.write(b'SIP/2.0 100 Trying\r\n')
            self.wfile.write(b'SIP/2.0 180 Ring\r\nSIP/2.0 200 OK\r\n\r\n')
        elif info.startswith('ACK'):
            pass #envío RTP
        elif info.startswith('BYE'):
            self.wfile.write(b'Finishing...')
        else:
            self.wfile.write(b'SIP/2.0 405 Method not Allowed\r\n\r\n')

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
