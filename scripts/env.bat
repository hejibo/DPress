@echo off
@call %~dp0..\python_env\Scripts\activate.bat
@set mg=python.exe %~dp0..\sites\manage.py
@cd %~dp0..\src
@cmd
