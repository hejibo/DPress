@echo off
set root_path=%~dp0../
set site_root=%root_path%site/
set lightco_path=%site_root%lightco/
xcopy "%root_path%apps\external_apps\filebrowser\media" "%root_path%static" /E/C/F/Y
python init_helper.py
