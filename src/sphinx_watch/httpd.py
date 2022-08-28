"""HTTP server module."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class HTTPServer(ThreadingHTTPServer):
    """Simple usage HTTP server.

    This is same implements of ``http.server`` module exec.
    """

    def __init__(self, port: int, directory: Path):  # noqa: D107
        bind = ("", port)
        super().__init__(bind, SimpleHTTPRequestHandler)
        self.directory = directory

    def finish_request(self, request, client_address):  # noqa: D102
        self.RequestHandlerClass(
            request, client_address, self, directory=self.directory
        )


def run_http_server(port: int, directory: Path):
    """Shor-hand of serve by HTTPServer."""
    with HTTPServer(port, directory) as httpd:
        httpd.serve_forever()
