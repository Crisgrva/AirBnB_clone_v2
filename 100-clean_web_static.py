#!/usr/bin/python3
"""
Deletes out-of-date archives,
using the function do_clean
"""

from os import listdir, remove
from fabric.api import local, env, run, put
from os.path import exists
from datetime import datetime

env.hosts = ['34.138.142.50', '54.196.190.217']


def do_clean(number=0):
    """
    Number is the number of the archives,
    including the most recent, to keep.
    If number is 0 or 1, keep only the most
    recent version of your archive.
    if number is 2, keep the most recent,
    and second most recent versions of your archive.
    """
    num_files = 1 if number == "0" or number == "1" else 2
    try:
        # Remote Files
        dir = "/data/web_static/releases/"
        string = run("for i in %s*; do echo $i; done" % dir)
        files = string.replace("\r", "").split("\n")
        files = sorted(files)[:-1] if num_files == 1 else sorted(files)[:-2]
        for file in files:
            if "web_static_" in file:
                run('rm -rf {}'.format(file))

        # LocalFiles
        Lfiles = listdir("versions")
        Lfiles = sorted(Lfiles)[:-1] if num_files == 1 else sorted(Lfiles)[:-2]
        for file in Lfiles:
            remove("versions/{}".format(file))

    except Exception as e:
        print(e)
