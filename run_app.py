#!/usr/bin/env python
# coding=utf-8

import os
from app import app

if __name__ == '__main__':
    port = os.environ.get("port", None)
    port = int(port) if port is not None else port
    app.run(
        host=os.environ.get("host", None),
        port=port,
        threaded=True
    )
