call base_init.bat
set /p var=please input app name:
python manage.py startapp %var%
