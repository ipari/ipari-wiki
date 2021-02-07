import threading

import config
from app import create_app
from app.watcher import PageWatcher


app = create_app(config)
watcher = PageWatcher()


if __name__ == '__main__':
    thread = threading.Thread(target=watcher.watch, args=())
    thread.daemon = True
    thread.start()

    app.run(
        threaded=True,
        # debug=True,
    )
