# Backup of docs/installation.md
# Created: 2025-09-29T15:45:09.223836
# Commit: 18982e439eb0819beae18a9f5b0177b3ea5c2ce8
# Message: Update calculator.py
# Author: Nipun Marwaha
# Original file: docs/installation.md
# Backup folder: backup/2025-09-29_15-45-00
# Full documentation backup

---

# Installation Guide

## System Requirements

- **Python Version**: 3.6 or higher
- **Operating System**: Windows, macOS, or Linux
- **Memory**: Minimum 128MB RAM
- **Disk Space**: Less than 1MB

## Installation Methods

### Method 1: Direct Download

1. **Download the repository:**
   ```bash
   git clone https://github.com/bluepal-nipun-marwaha/test-simple-repo.git
   cd test-simple-repo
   ```

2. **Verify Python installation:**
   ```bash
   python --version
   # Should output: Python 3.6.x or higher
   ```

3. **Run the calculator:**
   ```bash
   python calculator.py
   ```

### Method 2: Using pip (if available)

If the package is published to PyPI:

```bash
pip install simple-calculator
```

### Method 3: Virtual Environment (Recommended)

1. **Create virtual environment:**
   ```bash
   python -m venv calculator_env
   ```

2. **Activate virtual environment:**
   
   **Windows:**
   ```bash
   calculator_env\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   source calculator_env/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the calculator:**
   ```bash
   python calculator.py
   ```

## Dependencies

The calculator has minimal dependencies:

- **Python Standard Library**: No external packages required
- **requirements.txt**: Contains only basic development dependencies

### Current Dependencies
```
# Development dependencies only
pytest>=6.0.0
black>=21.0.0
flake8>=3.8.0
```

## Verification

After installation, verify the calculator works:

```bash
python calculator.py
```

You should see:
```
Simple Calculator
================

Options:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Show History
6. Clear History
7. Exit

Enter your choice (1-7):
```

## Troubleshooting

### Common Installation Issues

#### 1. Python Not Found
**Error:** `python: command not found`

**Solutions:**
- Install Python from [python.org](https://python.org)
- Add Python to your system PATH
- Use `python3` instead of `python`

#### 2. Permission Denied
**Error:** `Permission denied`

**Solutions:**
- Run with administrator/sudo privileges
- Use virtual environment
- Check file permissions

#### 3. Module Not Found
**Error:** `ModuleNotFoundError`

**Solutions:**
- Ensure you're in the correct directory
- Check Python version compatibility
- Reinstall dependencies

### Platform-Specific Issues

#### Windows
- Use Command Prompt or PowerShell
- Ensure Python is added to PATH
- Consider using Windows Subsystem for Linux (WSL)

#### macOS
- Use Terminal application
- May need to install Xcode Command Line Tools
- Consider using Homebrew for Python installation

#### Linux
- Use your distribution's package manager
- Ensure python3-dev packages are installed
- Check for missing system libraries

## Development Setup

For contributors and developers:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/bluepal-nipun-marwaha/test-simple-repo.git
   cd test-simple-repo
   ```

2. **Create development environment:**
   ```bash
   python -m venv dev_env
   source dev_env/bin/activate  # Linux/macOS
   # or
   dev_env\Scripts\activate     # Windows
   ```

3. **Install development dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run tests:**
   ```bash
   python -m pytest tests/
   ```

5. **Format code:**
   ```bash
   black calculator.py
   ```

6. **Lint code:**
   ```bash
   flake8 calculator.py
   ```

## Uninstallation

To remove the calculator:

1. **Delete the directory:**
   ```bash
   rm -rf test-simple-repo  # Linux/macOS
   rmdir /s test-simple-repo  # Windows
   ```

2. **Deactivate virtual environment:**
   ```bash
   deactivate
   ```

3. **Remove virtual environment:**
   ```bash
   rm -rf calculator_env  # Linux/macOS
   rmdir /s calculator_env  # Windows
   ```

## Support

If you encounter installation issues:

1. Check the [Issues](https://github.com/bluepal-nipun-marwaha/test-simple-repo/issues) page
2. Verify your Python version meets requirements
3. Try using a virtual environment
4. Check system-specific troubleshooting guides

