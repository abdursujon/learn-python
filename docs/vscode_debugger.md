## Debugging Python in VS Code

### 1. Install the extension
`Ctrl+Shift+X` → search `Python` → install the one by Microsoft.

### 2. Select the interpreter
`Ctrl+Shift+P` → `Python: Select Interpreter` → `./.venv/bin/python`

### 3. Call the code
A breakpoint inside a function is only hit if the function is called.

```python
def get_user(name, age):
    data = {"name": name, "age": age}   # breakpoint
    return data


get_user("Alice", 30)
```

### 4. Set a breakpoint
Click left of the line number. A red dot appears.

### 5. Start
`F5` → **Python Debugger** → **Python File**

### 6. Inspect and step
- **Variables** panel: current values
- Hover a variable in the editor to see its value
- **Debug Console**: evaluate expressions, e.g. `data["age"]`

| Key | Action |
|---|---|
| `F10` | Step over |
| `F11` | Step into |
| `Shift+F11` | Step out |
| `F5` | Continue |
| `Shift+F5` | Stop |

### Troubleshooting
| Symptom | Fix |
|---|---|
| Exits immediately | Breakpoint line never runs. Call the function. |
| Grey hollow breakpoint | Run the file that contains the breakpoint. |
| `ModuleNotFoundError` | Select the `.venv` interpreter (step 2). |
