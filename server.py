from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Simulacao concluida - dados nao armazenados")

server = HTTPServer(('localhost', 8080), Handler)
print("Servidor rodando...")
server.serve_forever()