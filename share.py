#!/usr/bin/python

import socket, sys
import SimpleHTTPServer
import SocketServer

try:
    PORT = int(sys.argv[1])
except:
    print "You need to specify a port number: share [port]"
    sys.exit()

url = socket.gethostbyname(socket.gethostname()) + ":"+str(PORT)
print "Share this link: " + "http://" + url

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

httpd.serve_forever()