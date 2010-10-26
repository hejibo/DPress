#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from helper import run, unzip
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = STATIC_FOLDER = os.path.join(HERE, "../")
TOOLS_FOLDER = os.path.join(ROOT, "tools/")
PYTHON_ENV = os.path.join(ROOT, "python_env/")
REQ_FOLDER = os.path.join(ROOT, "requirements/")
STATIC_FOLDER = os.path.join(ROOT, "sites/default/static/")

def do_unzip():
    print '== do_unzip =='
    #tools_zip_folder = os.path.join(TOOLS_FOLDER, "zip/")
    req_zip_folder = os.path.join(REQ_FOLDER, "zip/")
    unzip(os.path.join(req_zip_folder, "filebrowser.zip"), REQ_FOLDER)
    unzip(os.path.join(req_zip_folder, "grappelli.zip"), REQ_FOLDER)
    #static_scripts_folder = os.path.join(STATIC_FOLDER, 'scripts')

def do_pip():
    pip = os.path.join(PYTHON_ENV, "Scripts/pip.exe")
    if os.name == 'posix':
        pip = os.path.join(PYTHON_ENV, "bin/pip")
    print '== do_pip =='
    #TO_INSTALL_LIBS = ['Django','PIL','docutils','textile','Markdown']
    run('%s install %s' % (pip, 'Django==1.2.3'))
    run('%s install %s' % (pip, 'django-admin-tools'))
    run('%s install %s' % (pip, 'django-pagination'))
    run('%s install %s' % (pip, 'PIL'))
    run('%s install %s' % (pip, 'docutils'))
    run('%s install %s' % (pip, 'textile'))
    run('%s install %s' % (pip, 'Markdown'))

if __name__ == '__main__':
    #do_unzip()
    virtualenv_py = os.path.join(TOOLS_FOLDER, "virtualenv.py")
    print '== create PYTHON_ENV =='
    #run('python %s %s' % (virtualenv_py, PYTHON_ENV))
    do_pip()
