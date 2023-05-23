#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers """
import os
from fabric.api import hosts, put, run, env

env.hosts = ['54.236.12.12', '54.82.134.241']
def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if os.path.isfile(archive_path) == False:
            return False

    try:
        """Upload the archive to the /tmp/ directory in web server"""
        put(archive_path, '/tmp/')

        """Extract filename, Uncompress the archive and create directory"""
        f_name =  os.path.basename(archive_path)
        f_path = "/data/web_static/releases/" + f_name.split('.')[0]
        run("mkdir -p {}".format(f_path))
        run("tar -xzf /tmp/{} -C {}".format(f_name, f_path))
        
        """delete archive and symbolic link"""
        run("rm /tmp/{}".format(f_name))
        run("rm -rf /data/web_static/current")

        """Create new symbollic link"""
        run("ln -s {} /data/web_static/current".format(f_path))

        return True
    except:
        return False
