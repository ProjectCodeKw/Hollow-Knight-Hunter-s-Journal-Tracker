@echo off
title Hollow Knight Hunter's Journal Tracker
color 0A

echo ========================================
echo  Hollow Knight Hunter's Journal Tracker
echo ========================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    echo.
    pause
    exit /b 1
)

:: Check if required packages are installed
echo Checking dependencies...
python -c "import requests, PIL" >nul 2>&1
if errorlevel 1 (
    echo Installing required packages...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install required packages
        echo Please run: pip install -r requirements.txt
        echo.
        pause
        exit /b 1
    )
    echo Dependencies installed successfully!
    echo.
)

:: Check if save file path is configured
if not exist "HK_savefilepath.txt" (
    echo WARNING: HK_savefilepath.txt not found
    echo Please create this file with your Hollow Knight save file path
    echo Example: C:\Users\YourName\AppData\LocalLow\Team Cherry\Hollow Knight\user1.dat
    echo.
    pause
)

:: Check if images folder exists
if not exist "images" (
    echo WARNING: images folder not found
    echo Some enemy images may not display properly
    echo.
)

echo Starting application...
echo.
python START.py

if errorlevel 1 (
    echo.
    echo ERROR: Application crashed or encountered an error
    echo Please check the error message above
    echo.
    pause
    exit /b 1
)

echo.
echo Application closed successfully.
echo Press any key to exit...
pause >nul 