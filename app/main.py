import os, socket
from http.server import BaseHTTPRequestHandler, HTTPServer

VERSION = os.environ.get("APP_VERSION", "v1")
COLOR   = os.environ.get("APP_COLOR", "#2b6cb0")
POD     = os.environ.get("POD_NAME", socket.gethostname())

PAGE = """<!doctype html><html><head><meta charset="utf-8">
<title>CI/CD Demo</title><meta http-equiv="refresh" content="2">
<style>body{{font-family:system-ui,sans-serif;background:{color};color:#fff;
display:flex;height:100vh;margin:0;align-items:center;justify-content:center}}
h1{{font-size:5rem;margin:0 0 1rem;letter-spacing:-2px}}
p{{font-size:1.1rem;margin:.3rem;opacity:.85}}
code{{background:rgba(0,0,0,.25);padding:.15rem .5rem;border-radius:4px}}</style>
</head><body><div style="text-align:center">
<h1>{version}</h1><p>served by pod <code>{pod}</code></p>
</div></body></html>"""

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz":
            self.send_response(200); self.end_headers(); self.wfile.write(b"ok"); return
        b = PAGE.format(version=VERSION, color=COLOR, pod=POD).encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers(); self.wfile.write(b)
    def log_message(self, *a): pass

print(f"listening :8080 version={VERSION}", flush=True)
HTTPServer(("", 8080), H).serve_forever()
