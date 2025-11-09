#!/bin/bash
# Sure Health - Unix/Linux/Mac Run Script

echo "===================================="
echo "   Sure Health Web Application"
echo "===================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo ""
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo ""

# Install/Update requirements
echo "Checking dependencies..."
pip install -r requirements.txt --quiet
echo ""

# Check if model file exists
if [ ! -f "insurance_model.pkl" ]; then
    echo "WARNING: insurance_model.pkl not found!"
    echo "Please ensure the model file is in the project directory."
    echo "You can train the model by running: python model.py"
    echo ""
    read -p "Press enter to continue..."
fi

# Run the Flask application
echo "Starting Sure Health application..."
echo ""
echo "Application will be available at: http://localhost:5000"
echo "Press Ctrl+C to stop the server"
echo ""
python flask_app.py
