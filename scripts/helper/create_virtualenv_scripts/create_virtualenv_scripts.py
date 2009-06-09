"""
Call this like ``python fassembler/create-venv-script.py``; it will
refresh the fassembler-boot.py script
"""
import os
import subprocess
import re

here = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(here)
script_name = os.path.join(base_dir, 'dpress-boot.py')

import virtualenv

EXTRA_TEXT = """
TO_INSTALL_LIBS = ['Django','PIL','docutils','textile','Markdown']
TO_INSTALL_APPS = []
TO_INSTALLS = TO_INSTALL_LIBS + TO_INSTALL_APPS

def after_install(options, home_dir):
    if sys.platform == 'win32':
        bin = 'Scripts'
    else:
        bin = 'bin'
    for lib in TO_INSTALLS:
        subprocess.call([join(home_dir, bin, 'easy_install'),
                         lib])
"""

def main():
    text = virtualenv.create_bootstrap_script(EXTRA_TEXT, python_version='2.5')
    if os.path.exists(script_name):
        f = open(script_name)
        cur_text = f.read()
        f.close()
    else:
        cur_text = ''
    print 'Updating %s' % script_name
    if cur_text == 'text':
        print 'No update'
    else:
        print 'Script changed; updating...'
        f = open(script_name, 'w')
        f.write(text)
        f.close()

if __name__ == '__main__':
    main()
