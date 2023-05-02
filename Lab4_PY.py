from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib
import sys
import json
import requests

# https://localhost:8080/api_?func_v=x%5E2-2x&point_v=2

# Создаем обработчик запросов HTTPRequestHandler
class HTTPRequestHandler(BaseHTTPRequestHandler):
    # Метод для обработки GET-запросов
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/script.js':
            self.send_response(200)
            self.send_header('Content-type', 'text/javascript')
            self.end_headers()
            with open('script.js', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/style.css':
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            with open('style.css', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path.startswith('/api_'):
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET')
            self.send_header('Access-Control-Allow-Headers', 'Content-type')
            self.end_headers()
            query_components = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            func_v = query_components["func_v"]
            func_v = urllib.parse.quote(str(func_v).split("'")[1])

            point_v = query_components["point_v"]
            point_v = str(point_v).split("'")[1]
            
            
            api_url = f'https://newton.vercel.app/api/v2/tangent/{point_v}|{func_v}'
            response = requests.get(api_url)
            response_json = response.json()
            result = response_json.get('result')
            if result is not None:
                self.wfile.write(bytes(json.dumps(result), 'utf-8'))
            else:
                self.wfile.write(bytes(json.dumps('error'), 'utf-8'))

            
# Задаем настройки сервера (адрес и порт)
hostName = "localhost"
serverPort = int(sys.argv[1])

# python3 Lab4_Py.py 8080


# Создаем экземпляр HTTP сервера и запускаем его
httpd = HTTPServer((hostName, serverPort), HTTPRequestHandler)
print(f"Server started at http://{hostName}:{serverPort}")
httpd.serve_forever()