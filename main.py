import os
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=data["messages"],
            temperature=data.get("temperature", 0.8)
        )

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))