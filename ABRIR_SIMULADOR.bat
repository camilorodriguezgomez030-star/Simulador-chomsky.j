@echo off
cd /d "%~dp0"
python --version >nul 2>&1
if errorlevel 1 (
  echo Python no esta instalado o no esta agregado al PATH.
  echo Descargalo desde https://www.python.org/downloads/ y marca Add Python to PATH.
  pause
  exit /b 1
)
python -m pip install -r requirements.txt
if errorlevel 1 (
  echo No se pudieron instalar las dependencias.
  pause
  exit /b 1
)
python main.py
if errorlevel 1 pause
