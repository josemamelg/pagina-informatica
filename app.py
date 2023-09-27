import http.server
import socketserver

# Define el puerto en el que deseas ejecutar el servidor
PORT = 8000

# Crea un manejador que sirva los archivos desde el directorio actual
Handler = http.server.SimpleHTTPRequestHandler

# Inicia el servidor
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    # Comienza a servir
    httpd.serve_forever()
