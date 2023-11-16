import os

def get_root_folder():
    basedir = os.path.abspath(os.path.dirname(__file__))
    basedir = os.path.join(basedir, os.pardir)
    basedir = os.path.abspath(basedir)
    return basedir
