#!/usr/bin/python3
""" generates a .tgz archive from the contents of the web_static folder """

from datetime import datetime
from fabric.api import local


def do_pack():
    """ Package a directory and within it a .tgz file """

    sd = '{0:%Y%m%d%H%M%S}'.format(datetime.now())
    fname = 'versions/web_static_' + sd + '.tgz'
    local('mkdir -p versions')
    rs = local('tar -cvzf ' + fname + ' web_static')

    if rs.succeeded:
        return fname
    return None
