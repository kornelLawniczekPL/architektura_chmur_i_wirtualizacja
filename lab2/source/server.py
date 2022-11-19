#!/usr/bin/env python3
import http.server
import socketserver
import os
import time
from datetime import datetime, timedelta

#print('source code for "http.server":', http.server.__file__)

print(datetime.now())

class web_server(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):

        print(self.path)
        
        if self.path == '/':
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()            
            self.wfile.write(b"Hello World!\n")
        elif self.path == '/time':
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()            
            time = (datetime.now()  + timedelta(hours=1)).strftime('%H:%M:%S')
            self.wfile.write(str(time).encode('UTF-8'))

            #self.wfile.write(str(time.strftime('%H:%M:%S', time.localtime())).encoding('utf-8'))
            #self.wfile.write(str(time.strftime('%H:%M:%S', time.localtime())).encode('utf-8'))
            #self.wfile.write(f"{time}\n")
        else:
            super().do_GET()
    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
