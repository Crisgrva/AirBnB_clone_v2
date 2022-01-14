#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static
folder of your AirBnB Clone repo, using
the function do_pack.
"""
from fabric.api import local, env, run, put
from os.path import exists
from datetime import datetime

env.hosts = ['34.138.142.50', '54.196.190.217']


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
        path = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(path))
        print(path)
        return path
    except Exception as e:
        print(e)
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to your web
    servers, using the function do_deploy
    """

    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        # Example: versions/web_static_20220113185412.tgz
        # File = web_static_20220113185412
        file = archive_path.split('/')[-1].split('.')[0]
        run('mkdir -p /data/web_static/releases/{}/'.format(file))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}'
            .format(file, file))
        run('rm /tmp/{}.tgz'.format(file))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}'.format(file, file))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(file))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}\
            /data/web_static/current'.format(file))
        return True

    except Exception as e:
        print(e)
        return False


def deploy():
    """
    Creates and distributes an archive to your
    web servers, using the function deploy:
    """
    archive_path = do_pack()
    if archive_path is None:
        return False

    return(do_deploy(archive_path))
