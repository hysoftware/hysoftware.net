#!/usr/bin/env python
# coding=utf-8

import os
<<<<<<< HEAD
=======

>>>>>>> c4bf5ae19503d21e438e87b522b32bf698beaeec
from app import app

if __name__ == '__main__':
    app.run(
        host=os.environ.get("host", None),
        port=os.environ.get("port", None),
        threaded=True
    )
