# Log Analyzer System

## Project Overview
This project is a Log Analyzer System built using Python.  
It reads application log files, counts errors and warnings, detects corrupt lines, and generates a summary report in JSON format.  
Logging is implemented to track program execution, and exception handling ensures the program does not crash on corrupt or missing files.

---
## What Does This Project Do?
- Parses log files line by line
- Counts `ERROR` and `WARNING` log messages
- Detects and logs corrupt lines
- Generates a JSON summary report with total errors and warnings
- Logs all activities to console and log file
- Handles failures gracefully without stopping the program
---
##  Technologies Used
- Python 3
- os module
- json module
- logging module
---
## Project Structure

```
LOG_ANALYZER_SYSTEM/
│
├── inputs/         
│   └── app.log     # log file to analyze
│
├── outputs/        # output of analyzing
│   ├── log_analyzer.log
│   └── summary.json
│
├── src/
│   └── log_analyzer/
│       ├── __init__.py  #Package initializer
│       ├── log_analyzer.py # Main logic for analyzing logs
│       ├── logger.py # Logger configuration
│       ├── main.py  # Program entry point
│       └── parsing.py # Function to parse log lines
│
└── README.md  # project documentation

```

## How to Run
### 1. Clone the repository
```
git clone https://github.com/JaspinderKaurWalia26/PROJECT-7-Log-Analyzer-System.git
cd PROJECT-7-Log-Analyzer-System
```
### 2. Create a virtual environment (optional)
```
python -m venv venv
```
### 3. Activate the virtual environment
- Windows:
```
venv\Scripts\activate
```
- Linux/Mac:
```
source venv/bin/activate
```
### 4. Install dependencies
```
This project does not require any external dependencies.  
All required modules are part of Python’s standard library.
```
### 5. Run the program
```
python -m src.log_analyzer.main
```
### 6. Check outputs

- Summary Report: outputs/summary.json

- Logs: outputs/log_analyzer.log



