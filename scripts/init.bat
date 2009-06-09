@echo off
call helper/base_init.bat
python %root_path%scripts/helper/create_virtualenv_scripts/create_virtualenv_scripts.py
xcopy "%root_path%apps\external_apps\filebrowser\media" "%root_path%static" /E/C/F/Y
python %root_path%scripts/helper/init_helper.py
python %root_path%scripts/helper/dpress-boot.py %root_path%dpress-env/
