# Pytest Fundamentals 

- Installing Pytest 
```bash
python3 -m venv .venv
source .venv/bin/activate 
pip install pytest 
```

- Running a test 
```bash
cd directory_name 
pytest test_one.py
```

- Getting extra information about test failure 
```bash
cd directory_name 
pytest -v test_one.py 
pytest -vv test_one.py
```

- Turn off traceback 
```bash
cd directory_name 
pytest --tb=no test_one.py
```

- Run multiple test script at the same time 
```bash
pytest --tb=no
```

- Show printed value inside the tests
```bash
pytest -s 
pytest file_name -s 
```

- Stop python creating pytest_cache
```bash
PYTHONDONTWRITEBYTECODE=1
```

--- 

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

--- 

# Topics to Cover
1. Assertions
2. Exceptions
3. Fixtures
4. Builtin fixtures
5. Parametrize
6. Markers
7. Test strategy
8. Configuration files
9. Coverage
10. tox and CI
    - tox runs your test suite in several isolated environments, for example Python 3.10, 3.11 and 3.12
    - CI (Continuous Integration) runs tests automatically on a server, such as GitHub Actions, on every push or open a pull request.
11. Testing scripts
    - Allows running pytest from any directory
12. Debugging
```bash
pytest -x               # stop on first failure
pytest --lf             # rerun last failed
pytest -l               # show local variables
pytest --pdb            # drop into debugger on failure
pytest -k "mango"       # run tests matching name
```
13. Advanced parametrize