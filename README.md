# Learn Python
The aim of this project is to explore Python fundamentals and data structures with practical examples. The project is kept simple and beginner-friendly, so it can be used as a guide to learn Python with no prior experience. It also covers the fundamentals of using Pytest to test your code.

--- 

### How to Install Python on Windows

### Step 1: Download Python
Go to python.org
Click Downloads → Select the latest Python version
Download the .exe installer

### Step 2: Run Installer
Double-click the downloaded file
Check the box: "Add Python to PATH"
Click Install Now and wait for the installation to complete

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

After the last command, you should see a Python version such as 3.12.0.

--- 

## Fundamentals Topics Covered
- **chapter_1:** Data Types, Operators, Variables
- **chapter_2:** Conditionals, Loops
- **chapter_3:** Functions, Input/Output, Formatting
- **chapter_4:** Math Functions, Random
- **chapter_5:** Exceptions, File Input/Output, Storing Data
- **chapter_6:** Object-Oriented Programming (OOP)
- **chapter_7:** String, Regex
- **chapter_8:** Lambda, List Comprehension
- **chapter_9:** Built-in Functions

--- 

## Data Structures Covered (shortcut to remember: alt dict ssd)
- list
- array 
- dictionary 
- set 
- tuple 
- frozenset 
- string 
- deque 


--- 

## Testing: Pytest 
- **Testing a class**
- **Testing a function**


--- 

## Common Python Setup I Use 
- IDE: VS Code 
```bash
sudo snap install code --classic 
sudo snap refresh code # update VS Code 

# alternative method 
sudo apt update
sudo apt install --only-upgrade code
```

- Python version manager: pyenv (when a project needs a Python version different from the one installed on the system, pyenv installs that version for the project without changing the system-wide version)
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
```bash
pip install mypy
mypy .            # check the whole project
mypy main.py      # check one file
mypy file_name --strict
```

- Testing: pytest and unittest.mock
```bash
pip install pytest
```

- Pre-commit hooks: pre-commit (runs checks like Ruff automatically on every git commit and blocks the commit if they fail)
  - Needs a `.pre-commit-config.yaml` file in the project root that lists which checks to run. Without it, nothing runs.
```bash
pip install pre-commit
pre-commit install    # once per repo, turns on the Git hook
```

- Debugging: VS Code debugger
```bash
code --install-extension ms-python.python
```

- Logging: logging 
```bash
import logging 
```

- Error tracking: Sentry (catches errors from your app running in production and sends you alerts with the full traceback)
```bash
pip install sentry-sdk
```

- Profiling: cProfile (shows how many times each function runs and how long it takes, so you can find slow code)
```bash
python3 -m cProfile -s cumtime YOUR_SCRIPT.py
```

- Version control: Git
```bash
sudo apt install git
```


- CI/CD: GitHub Actions (workflow files can have any name but must end with .yml)
```
my-project/
└── .github/
    └── workflows/
        └── ci.yml
        └── cd.yml
```

- Containers: Docker
```bash
sudo apt install docker.io
sudo usermod -aG docker $USER   # adds you to the docker group so you can run docker without sudo (log out/in after)
```

- Deployment: AWS
```bash
sudo snap install aws-cli --classic   # installs the AWS command-line tool
aws configure                         # connects your terminal to your AWS account
```
  - `aws configure` asks for an Access Key ID and Secret Access Key. Create them on the AWS website under IAM → your user → Security credentials.

- Docs from .md files
```bash
pip install mkdocs
mkdocs new .       # creates mkdocs.yml and a docs/ folder
mkdocs serve       # opens the site at http://127.0.0.1:8000
```