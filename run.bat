@echo off
REM Sure Health - Windows Run Script

echo ====================================
echo    Sure Health Web Application
echo ====================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate
echo.

REM Install/Update requirements
echo Checking dependencies...
pip install -r requirements.txt --quiet
echo.

REM Check if model file exists
if not exist "insurance_model.pkl" (
    echo WARNING: insurance_model.pkl not found!
    echo Please ensure the model file is in the project directory.
    echo You can train the model by running: python model.py
    echo.
    pause
)

REM Run the Flask application
echo Starting Sure Health application...
echo.
echo Application will be available at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
python flask_app.py

pause
