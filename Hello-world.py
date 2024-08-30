# /home/sharjeel/Music/A/B/app.py

import http.server
import socketserver

# Define the port on which the server will run
PORT = 3000

# Custom handler to serve a simple Hello World HTML page
class HelloWorldHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Set the response status code to 200 (OK)
        self.send_response(200)
        
        # Set the content type to HTML
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # Define the HTML content
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Hello World</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>This is a simple web page served by a Python HTTP server running in a Docker container.</p>
        </body>
        </html>
        """
        
        # Write the HTML content to the response
        self.wfile.write(html_content.encode("utf-8"))

# Set up the server with the custom handler
with socketserver.TCPServer(("", PORT), HelloWorldHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()

