import sys
import os
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

HandlerClass = SimpleHTTPRequestHandler
ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.1"

if sys.argv[1:]:
  
    port = int(sys.argv[1])

else:
  
    port = 80

server_address = ('0.0.0.0', port)
sys.stderr = open("log/server-activity.veil", "w")

try:

	os.chdir("html/")
	HandlerClass.protocol_version = Protocol
	httpd = ServerClass(server_address, HandlerClass)
	sa = httpd.socket.getsockname()
	print "Serving HTTP on", sa[0], "port", sa[1], "...\nPress Ctrl+Z to stop"

	httpd.serve_forever()


except Exception:

	conn.close()
	httpd.server_close()