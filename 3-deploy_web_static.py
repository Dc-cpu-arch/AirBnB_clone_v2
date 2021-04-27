#!/usr/bin/python3
""" Fabirc Script - creates and distribute files to web servers """

from fabric.api import put, run, env, local
from os.path import exists, basename, splitext
from datetime import datetime
from os import makedirs

time = datetime.now()
env.hosts = ['35.231.124.90', '34.73.164.166']
env.user = 'ubuntu'


def do_pack():
    """ Creates an archive of web_static with .tgz format """
    makedirs('versions', exist_ok=True)
    date = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(
            time.year, time.month, time.day, time.minute, time.second)
    check = local("tar -cvzf " + date + " ./web_static/")
    if check.succeeded:
        return date
    return None


def do_deploy(archive_path):
    """ distributes files between servers """

    if os.path.exists(archive_path):

        put(archive_path, "/tmp/")
        filename = os.path.basename(archive_path)
        (file, ext) = os.path.splitext(filename)
        rel_path = "/data/web_static/releases/"
        run("mkdir -p {}{}/".format(rel_path, file))
        run("tar -xzvf /tmp/{} -C {}{}/".format(filename, rel_path, file))
        run("rm -f /tmp/{}".format(filename))
        run("mv {}{}/web_static/* {}{}/".format(rel_path, file,
                                                rel_path, file))
        run("rm -rf {}{}/web_static".format(rel_path, file))
        run("rm -rf /data/web_static/current")
        run("ln -sf {}{}/ /data/web_static/current".format(rel_path, file))

        return True
    return False


def deploy():
    """ creates and distributes files """
    packing = do_pack()
    if packing is False:
        return False

    return do_deploy(packing)
