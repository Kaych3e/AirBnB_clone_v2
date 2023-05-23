#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers """
import os
from fabric.api import hosts, put, run, env

env.hosts = ['54.236.12.12', '54.82.134.241']
def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    try:
        if os.path.isfile(archive-path) == False:
            return False

        """Upload the archive to the /tmp/ directory and extract file name"""
        put(archive_path, '/tmp/')
        f_name = archive_path.split('/')[-1].split('.')[0]

        """Uncompress the archive and create directory"""
        f_path = "/data/web_static/releases/{}".format(f_name)
        run("mkdir {}".format(f_path))
        run("tar -xzf /tmp/{archive_path.split('/')[-1]} -C {}".format(f_path))
        
        """delete archive and symbolic link"""
        run("rm /tmp/{}".format(archive_path.split('/')[-1]))
        run("rm /data/web_static/current")

        """Create new symbollic link"""
        run("ln -s {} /data/web_static/current".format(f_path))

        return True
    except:
        return False
