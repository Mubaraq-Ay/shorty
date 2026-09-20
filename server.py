from http.server import HTTPServer, BaseHTTPRequestHandler
import sqlite3

conn = sqlite3.connect('url.db')
cursor = conn.cursor()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)

        short_code = self.path.lstrip("/")
        
        cursor.execute("""
            SELECT * FROM urls
            WHERE short_code = ?
        """, (short_code,))

        result = cursor.fetchone()

        if result is not None:
            self.send_response(302)
            self.send_header("Location", result[0])
            self.end_headers()
        elif result is None:
            print('not found.')
   


server = HTTPServer(("localhost", 8000), Handler)
server.serve_forever()
