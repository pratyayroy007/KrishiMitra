@echo off
title Krishi Mitra Server
echo ========================================================
echo   Starting Krishi Mitra Agricultural AI Extension Agent
echo ========================================================
echo.
cd /d "%~dp0"

echo Launching browser at http://localhost:5000 in 2 seconds...
start "" timeout /t 2 /nobreak >nul & start http://localhost:5000

echo Starting Flask server on http://localhost:5000...
echo (Press CTRL+C anytime in this window to stop the server)
echo.
python app.py
pause
