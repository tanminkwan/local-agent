import daemon
import signal
import sys
from flask import Flask

def run_flask_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello, world!"

    app.run(host="0.0.0.0", port=8808, debug=True)

def run_as_daemon():
    with daemon.DaemonContext():
        run_flask_app()

def handle_signal(signum, frame):
    sys.exit(0)

if __name__ == '__main__':
#    signal.signal(signal.SIGTERM, handle_signal)
#    signal.signal(signal.SIGINT, handle_signal)
    run_as_daemon()