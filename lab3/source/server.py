#!/usr/bin/env python3
import http.server
import socketserver
import os
#import time
from datetime import datetime, timedelta
import re

#print('source code for "http.server":', http.server.__file__)

def conting_signs(string):

    out_dict = {'lowercase': 0, 'uppercase': 0, 'digits': 0, 'special': 0}
    regex = re.compile(r"[@_!#$%^&*()<>?/\|}{~:]")

    for sign in string:
        if sign.islower():
            out_dict['lowercase'] += 1
        elif sign.isupper():
            out_dict['uppercase'] += 1
        elif sign.isdigit():
            out_dict['digits'] += 1
        elif regex.search(sign):
            out_dict['special'] += 1

    print(out_dict)
    return out_dict


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
            # CZAS ZIMOWY ( +1H ) 
            time = (datetime.now()  + timedelta(hours=1)).strftime('%H:%M:%S')
            self.wfile.write(str(time).encode('UTF-8'))
        elif self.path.startswith('/rev?'):
            temporary_string = self.path.split("?")[1]
            temporary_string = str(temporary_string[::-1])
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()
            self.wfile.write(temporary_string.encode('utf-8'))
        else:
            super().do_GET()
    
# --- main ---

PORT = 4080


print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
