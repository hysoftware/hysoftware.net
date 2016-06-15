#!/usr/bin/env python
# coding=utf-8

import os
import getpass

from flask.ext.script import Manager, Server

from app import app
import app.user.models as user


port = os.environ.get("port", None)
port = int(port) if port is not None else port
manager = Manager(app)
manager.add_command(
    "runserver",
    Server(host=os.environ.get("host", None), port=port, threaded=True)
)

@manager.command
def add_superuser():
    """Add a superuser."""
    admin = user.Person.objects(role__in=["admin"])
    if len(admin) > 0:
        raise ValueError("There's already an admin!")
    model = user.Person(role=["admin"])
    model.firstname = input("First Name? ")
    model.lastname = input("Last Name? ")
    model.email = input("email? ")
    model.password = getpass.getpass()
    model.is_authenticated = True
    model.is_active = True
    model.save()
    print("Done.")

if __name__ == '__main__':
    manager.run()
