import http.server
import socketserver
import os
import functools

ROOT = "/private/tmp/claude-502/-Users-yurii-kravtsov-Downloads-Test-project/284f4711-c52f-42c7-8f3a-e962073f8f7d/scratchpad/preview"

Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT)

with socketserver.TCPServer(("127.0.0.1", 4173), Handler) as httpd:
    httpd.serve_forever()
