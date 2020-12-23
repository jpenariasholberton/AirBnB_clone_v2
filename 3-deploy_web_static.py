#!/usr/bin/python3
""" """


from fabric.api import *
import os.path as path
from datetime import datetime


env.hosts = ['35.243.150.179', '35.227.36.71']


def do_pack():
    """ Package a directory and within it a .tgz file """

    sd = '{0:%Y%m%d%H%M%S}'.format(datetime.now())
    fname = 'versions/web_static_' + sd + '.tgz'
    local('mkdir -p versions')
    rs = local('tar -cvzf ' + fname + ' web_static')

    if rs.succeeded:
        return fname
    return None


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


def deploy():
    """ Deploy to servers """
    file_path = do_pack()
    if not file_path:
        return False
    return do_deploy(file_path)
