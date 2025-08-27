@echo off
title Home Instead Raffle Dashboard
echo.
echo 🏠 Home Instead Professional Raffle Dashboard
echo =============================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo.
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo ✅ Python found
echo.

:: Try to install dependencies if they don't exist
echo 📦 Checking dependencies...
python -c "import flask, bcrypt, jwt" >nul 2>&1
if errorlevel 1 (
    echo Installing required packages...
    python -m pip install Flask python-dotenv bcrypt PyJWT Flask-Limiter openpyxl Flask-CORS
    if errorlevel 1 (
        echo ❌ Failed to install packages
        echo Try running as Administrator or use: python -m pip install --user [packages]
        pause
        exit /b 1
    )
)

echo ✅ Dependencies ready
echo.

:: Check if .env exists
if not exist ".env" (
    echo 🔧 Setting up configuration...
    if exist ".env.example" (
        copy ".env.example" ".env" >nul
        echo ✅ Environment configuration created
    )
)

echo 🚀 Starting dashboard...
echo.
echo Dashboard will be available at: http://localhost:5000
echo Default login: admin@homeinstead.com / admin123
echo.
echo Press Ctrl+C to stop the server
echo.

:: Start the application
python app.py

if errorlevel 1 (
    echo.
    echo ❌ Application failed to start
    echo Check the error messages above
    echo.
    pause
)

echo.
echo Dashboard stopped.
pause