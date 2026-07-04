# Student Local Python Setup

This guide helps students prepare a local Python environment for ANL559 - AI Agents for Analytics Automation.

Students can complete the early labs with spreadsheets, but a local Python setup is recommended if the class will run scripts, notebooks, tests, or model examples on student laptops.

## What Students Need

- Python 3.10 or later.
- A terminal: PowerShell on Windows, Terminal on macOS.
- A code editor such as VS Code.
- The course folder from GitHub or the LMS.

The course uses these core packages:

- `pandas` and `numpy` for data work.
- `scikit-learn` for simple modelling in Week 3.
- `matplotlib` for quick charts.
- `jupyterlab` for notebooks.
- `pytest` for simple tests and checks.

## Windows Setup

### 1. Install Python

Install Python 3.10 or later from the official Python website or from your institution's approved software center.

During installation, select:

```text
Add python.exe to PATH
```

Then open a new PowerShell window and check:

```powershell
python --version
```

If `python` is not found, try:

```powershell
py --version
```

### 2. Open The Course Folder

In PowerShell:

```powershell
cd "C:\path\to\AI_Analytics_Studio_Refresh"
```

Replace the path with the folder on your laptop.

### 3. Create A Virtual Environment

```powershell
python -m venv .venv
```

If your machine uses the Python launcher:

```powershell
py -m venv .venv
```

### 4. Activate The Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

When active, the prompt usually starts with:

```text
(.venv)
```

### 5. Install Course Packages

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 6. Run The Setup Check

```powershell
python scripts\check_python_setup.py
```

You should see PASS for Python and the required packages.

### 7. Run The Week 1 Example

```powershell
python Starter_Kit\examples\week1_kpi_smoke_checks.py
```

Expected final line:

```text
All checks passed.
```

## macOS Setup

### 1. Install Python

Install Python 3.10 or later from the official Python website, Homebrew, or your institution's approved software center.

Check the version:

```bash
python3 --version
```

### 2. Open The Course Folder

```bash
cd "/path/to/AI_Analytics_Studio_Refresh"
```

### 3. Create And Activate A Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Course Packages

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Run The Setup Check

```bash
python scripts/check_python_setup.py
```

### 6. Run The Week 1 Example

```bash
python Starter_Kit/examples/week1_kpi_smoke_checks.py
```

Expected final line:

```text
All checks passed.
```

## VS Code Recommendation

Students using VS Code should install:

- Python extension.
- Jupyter extension.

Then open the course folder in VS Code:

```text
File > Open Folder > AI_Analytics_Studio_Refresh
```

When VS Code asks for a Python interpreter, choose the one inside `.venv`.

## Common Problems

### `python` is not recognized

Close and reopen PowerShell after installing Python. If that still fails, use:

```powershell
py --version
py -m venv .venv
```

### Activation is blocked on Windows

Run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Package installation fails

Try upgrading pip:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If it still fails, copy the error message and bring it to class. The learning objective is not to become a Python installation expert; ask for help early.

### The Week 1 script cannot find CSV files

Make sure you run the command from the course folder:

```text
AI_Analytics_Studio_Refresh
```

The script expects the sample files under:

```text
Starter_Kit/sample_data/
```

## Instructor Setup Check

Before Week 1, ask students to submit a screenshot or text output from:

```powershell
python scripts\check_python_setup.py
python Starter_Kit\examples\week1_kpi_smoke_checks.py
```

This catches setup problems before the first studio sprint.

