#!/bin/bash

cd /path/to/your/project
# create virtual environment

python3 -m venv venv
# Activate virtual environment
source venv/bin/activate

# Install dependencies using pip
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Deactivate the virtual environment
deactivate