#!/usr/bin/python3
""" distributes an archive to your web servers """

from fabric.api import *
import os.path as path


env.hosts = ['35.243.150.179', '35.227.36.71']


def do_deploy(archive_path):
    """ Deploy to servers """

    if not path.exists(archive_path):
        return False
    try:
        filename = archive_path.split("/")[-1]
        noext = filename.split(".")[0]
        put(archive_path, '/tmp/{}'.format(filename))
        run('mkdir -p /data/web_static/releases/{}/'.format(noext))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(filename, noext))
        run('rm /tmp/{}'.format(filename))
        run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/".format(noext, noext))
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(noext))

        run('rm -rf /data/web_static/current')
        run('ln -sf /data/web_static/releases/{}/ \
            /data/web_static/current'.format(noext))
        return True
    except Excepction:
        return False
