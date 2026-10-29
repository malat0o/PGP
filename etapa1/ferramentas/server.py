import http.server, os, sys, urllib.parse
ROOT = os.path.abspath(sys.argv[1])
class H(http.server.SimpleHTTPRequestHandler):
    def __init__(s, *a, **k): super().__init__(*a, directory=ROOT, **k)
    def do_POST(s):
        q = urllib.parse.parse_qs(urllib.parse.urlparse(s.path).query)
        rel = q["name"][0].replace("\\", "/")
        dest = os.path.abspath(os.path.join(ROOT, rel))
        if not dest.startswith(os.path.join(ROOT, "etapa1")) or ".." in rel:
            s.send_response(403); s.end_headers(); return
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "wb").write(s.rfile.read(int(s.headers["Content-Length"])))
        s.send_response(200); s.end_headers(); s.wfile.write(b"ok")
http.server.ThreadingHTTPServer(("127.0.0.1", 8765), H).serve_forever()
