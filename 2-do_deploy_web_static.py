#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers """
import os
from fabric.api import hosts, put, run

env.hosts = ['54.236.12.12', '54.82.134.241']
def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    try:
        if os.path.isfile(archive-path) == False:
            return False

        """Upload the archive to the /tmp/ directory and extract file name"""
        put(archive_path, '/tmp/')
        f_name = archive_path.split('/')[-1].split('.')[0]

        """Uncompress the archive and create directory"""
        f_path = f"/data/web_static/releases/{f_name}"
        run(f"mkdir {f_path}")
        run(f"tar -xzf /tmp/{archive_path.split('/')[-1]} -C {f_path}")
        
        """delete archive and symbolic link"""
        run(f"rm /tmp/{archive_path.split('/')[-1]}")
        run("rm /data/web_static/current")

        """Create new symbollic link"""
        run(f"ln -s {f_path} /data/web_static/current")

        return True
    except:
        return False
