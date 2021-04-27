#!/usr/bin/python3
""" Fabric script that compress the web_static directory in .tgz"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Compress in tgz format"""
    try:
        date = datetime.now().strftime('%Y%m%d%H%M%S')
        local("mkdir -p versions")
        name = "web_static_" + date + ".tgz"
        path = "versions/" + name
        local("tar -cvzf {} web_static".format(path))
        return path
    except Exception:
        return None
