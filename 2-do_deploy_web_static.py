#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers """
import os
from fabric.api import *
from datetime import datetime

def do_pack():
    """ Create tar archive of web_static directory """
    if os.path.isdir("versions") is False:
        if local('mkdir -p versions').failed is True:
            return None

    t = datetime.utcnow()
    f_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(t.year,
                                                           t.month,
                                                           t.day,
                                                           t.hour,
                                                           t.minute,
                                                           t.second)

    with cd("versions"):
        if local("tar -cvzf {} web_static".format(f_name)).failed is True:
            return None

        return f_name


env.hosts = ['54.236.12.12', '54.82.134.241']


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if os.path.isfile(archive_path) is False:
            return False

    try:
        """Upload the archive to the /tmp/ directory in web server"""
        put(archive_path, '/tmp/')

        """Extract filename, Uncompress the archive and create directory"""
        f_name =  os.path.basename(archive_path)
        f_path = "/data/web_static/releases/" + f_name.split('.')[0]
        run("mkdir -p {}".format(f_path))
        run("tar -xzf /tmp/{} -C {}".format(f_name, f_path))

        """delete archive and symbolic link fro the web server"""
        run("rm /tmp/{}".format(f_name))
        run("mv /data/web_static/releases/{}/web_static/*\
                /data/web_static/releases/{}/".format(f_name, f-name))
        run("rm -rf /data/web_static/current")

        """Create new symbollic link"""
        run("ln -s {} /data/web_static/current".format(f_path))

        return True
    except:
        return False
