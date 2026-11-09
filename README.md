# Learn Python
The aim of this project is to explore python fundamentals and data structures with practical examples. The project is kept simple and beginner friendly which could be utilised as a guide to learn python with no prior experience. It also cover fundamental of how to use Pytest to test your 
code.

--- 

### How to Install Python on  Windows

### Step 1: Download Python
Go to python.org
Click Downloads → Select latest Python version
Download the .exe installer

### Step 2: Run Installer
Double-click the downloaded file
Check the box: "Add Python to PATH"
Click Install Now and wait for installation to complete

### Step 3: Verify Installation
Open Command Prompt and run this command: python --version
You should see something like: Python 3.12.0

--- 

### How to Install Python on Linux 
Run these commands one after another. 

```bash
sudo apt update 
sudo apt install python3
python3 --version
```

After last command you should see a version of python such as 3.12.0

--- 

## Fundamentals Topics Covered
- **chapter_1:** Data Types, Operators, Variables
- **chapter_2:** Conditionals, Loops
- **chapter_3:** Functions, Input/Output
- **chapter_4:** Built-in Functions, Math Functions
- **chapter_5:** Exceptions, File Input/Output, Storing Data
- **chapter_6:** Object-Oriented Programming (OOP)
- **chapter_7:** String, Regex
- **chapter_8:** Lambda

--- 

## Data Structures Covered (shortcut to remember: alt dict ssd)
- list
- array 
- dictionay 
- set 
- tuple 
- frozenset 
- string 
- deque 

## Testing: Pytest 
- **Testing a class**
- **Testing a function**

## Python Common Set Up I Use 
- IDE: VS Code 
```bash
sudo snap install code --classic 
```

- Python version manager: pyenv (When we work on a project that is not similar to version we have in the system this install that version without having to change our entire version for that project)
```bash
# one-time setup
sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev curl git
curl -fsSL https://pyenv.run | bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init - bash)"' >> ~/.bashrc
source ~/.bashrc
```
```bash
# per project that needs a different Python version
cd project_we_are_working_on
pyenv install 3.10      # download and build Python 3.10 (once per version)
pyenv local 3.10        # use 3.10 in this project folder
python -m venv .venv    # create the venv with that version
```

- Env & packaging: venv
```bash
sudo apt install python3-venv
python3 -m venv .venv
source .venv/bin/activate
```

- Linting & formatting: Ruff
```bash
pip install ruff
ruff check .          # find problems (unused imports, bad patterns, etc.)
ruff check file_name 
ruff check . --fix    # find and auto-fix what it can
ruff check file_name --fix 
ruff format .         # format the code (spacing, quotes, line length)
ruff format file_name
```

- Type checking: mypy
- Testing: pytest and unittest.mock
- Pre-commit hooks: pre-commit (runs checks like Ruff automatically on every git commit and blocks the commit if they fail)
- Debugging: VS Code debugger
- Logging: logging 
- Error tracking: Sentry (catches errors from your app running in production and sends you alerts with the full traceback)
- Profiling: cProfile 
- Version control: Git
- CI/CD: GitHub Actions
- Containers: Docker
- Deployment: AWS
- Docs: Sphinx / MkDocs