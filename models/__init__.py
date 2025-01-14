#!/usr/bin/python3
"""This module instantiates an instance of FileStorage"""
from os import getenv

storage_type = getenv('HBHB_TYPE_STORAGE')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
