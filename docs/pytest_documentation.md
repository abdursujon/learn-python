# Setup virtual environment for pip upgrade 
- cd project_path 
- create vertual eneronment in current directory: python3 -m venv venv
- activate venv: source venv/bin/activate 
- deactivate venv: deactivate


# Update pip (Python utilises pip to install third party packages such as pytest, matplotlib)
- Update pip: python3 -m pip install --upgrade pip

# Install pytest 
python3 -m pip install pytest 

# Updating any third party application
python3 -m pip install --upgrade package_name 