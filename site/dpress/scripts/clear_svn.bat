@echo off
cd ..
set /p var=do you want remove all .svn folder?!(y/n):
if "%var%" == "y" for /r /d %%D in (.svn) do @rmdir /q /s "%%D"
