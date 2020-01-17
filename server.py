from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        res_body = {
            'message': 'What a great request you just made, I\'m so proud of you.'
        }

        json_body = json.dumps(res_body)

        self.wfile.write(json_body.encode('utf_8'))

try:
    PORT = 80
    server = ThreadingHTTPServer(('', PORT), Handler)
    print('Server started on {}'.format(PORT))
    server.serve_forever()
except KeyboardInterrupt:
    print ('shutting down server')
    server.socket.close()