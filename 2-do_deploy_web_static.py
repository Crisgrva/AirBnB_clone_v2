#!/usr/bin/python3
"""
Fabric script
(based on the file 1-pack_web_static.py)
"""
from fabric.api import env, run, put
from os.path import exists

env.hosts = ['34.138.142.50', '54.196.190.217']


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
        return False
