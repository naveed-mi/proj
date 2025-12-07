#!/usr/bin/env python3

import datetime
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

class SimpleTimeHandler(BaseHTTPRequestHandler):
    def _get_client_ip(self):
        xff = self.headers.get("X-Forwarded-For")
        if xff:
            return xff.split(",")[0].strip()
        return self.client_address[0]

    def _send_json(self, payload: dict, status: int = 200):
        # Pretty printed JSON (2-space indent)
        body = json.dumps(payload, indent=2).encode("utf-8")

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path not in ("/", ""):
            self.send_error(404, "Not Found")
            return

        now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
        client_ip = self._get_client_ip()

        response = {
            "timestamp": now_utc,
            "ip": client_ip,
        }
        self._send_json(response)

    def log_message(self, format, *args):
        print("%s - - [%s] %s" % (
            self.address_string(),
            self.log_date_time_string(),
            format % args
        ))

def run_server():
    port = int(os.environ.get("PORT", "8080"))
    server_address = ("0.0.0.0", port)
    httpd = ThreadingHTTPServer(server_address, SimpleTimeHandler)
    print(f"SimpleTimeService listening on port {port}", flush=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()

if __name__ == "__main__":
    run_server()
