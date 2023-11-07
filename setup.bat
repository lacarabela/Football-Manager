@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

REM Check for Python and encourage install if not present
WHERE python >nul 2>&1
IF !ERRORLEVEL! NEQ O (
    ECHO Python is not installed.
    ECHO Please install Python from https://www.python.org/downloads/ and rerun this script.
    EXIT /B 1
)

REM Check for pop and install if not exists
python -m ensurepip --upgrade

REM Install required packages
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

ECHO Installation completed succesfully.
pause
