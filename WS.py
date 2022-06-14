import socketserver
import time
import http.server
import requests 

print("Starting...")
mainport = 4748
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", mainport), Handler) as httpd:
    httpd.serve_forever()
