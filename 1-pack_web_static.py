#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static
folder of your AirBnB Clone repo, using
the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    The function do_pack must return
    the archive path if the archive has
    been correctly generated. Otherwise,
    it should return None
    """
    try:
        local('mkdir -p versions')
        date = str(datetime.now().strftime("%Y%m%d%H%M%S"))
        path = "versions/web_static_{}".format(date)
        local("tar -cvzf {}.tgz web_static".format(path))
        return path
    except Exception as e:
        return None
