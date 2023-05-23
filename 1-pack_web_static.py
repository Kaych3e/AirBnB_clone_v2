#!/usr/bin/python3
""" Generates a .tgz archive from the contents of web_static with Fabric"""

import os.path
from datetime import datetime
from fabric.api import local
from fabric.context_managers import cd

def do_pack():
    """ Create tar archive of web_static directory """
    if os.path.isdir("versions") == False:
        if local('mkdir -p versions').failed == True:
            return None

    t = datetime.utcnow()
    f_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(t.year,
                                                           t.month,
                                                           t.day,
                                                           t.hour,
                                                           t.minute,
                                                           t.second)

    with cd("versions"):
        if local("tar -cvzf {} web_static".format(f_name)).failed == True:
            return None

        return f_name
