# Windows Setup for SALLM Test Evaluation

## Overview
The `run_tests.py` script has been updated to run on Windows with GPT-generated Python files from the `Generation/Filtered_Output/` directory.

## Changes Made

### 1. Updated `config.py`
- **Fixed paths**: Now uses proper path joining that works on Windows
- **Improved directory references**: Uses clearer BASE_DIR and ROOT_DIR variables
- **Added TEST_FOLDER**: New output folder for test files

### 2. Updated `run_tests.py`

#### Docker Detection (Windows Compatible)
- Detects OS platform using `sys.platform`
- On macOS: Checks for `/Applications/Docker.app/...`
- On Windows: Uses `docker` command directly (must be in PATH from Docker Desktop)
- On Linux: Uses `docker` command directly

#### Path Handling for Docker on Windows
- Converts Windows paths (`\`) to forward slashes (`/`) for Docker
- Handles both absolute and relative paths correctly
- Uses `replace("\\", "/")` for Windows path conversion

#### Exception Handling
- Improved error handling for container name generation (removes forward slashes on Windows)
- Better cleanup of temporary report directories

#### Folder Management
- Now creates `test` folder
- Creates `TestModelResults` folder
- Creates `TestResults` folder
- All folders are created at startup with proper messages

### 3. Created Required Directories
```
c:\Users\msiddiq3\SALLM\Evaluation\test
c:\Users\msiddiq3\SALLM\Evaluation\TestModelsResults
c:\Users\msiddiq3\SALLM\Evaluation\TestResults
```

## Running the Script on Windows

### Prerequisites
1. Docker Desktop installed and running
2. Docker command available in system PATH
3. Base images built (script will attempt to build if not present)

### To Run Tests on GPT Files
```bash
cd c:\Users\msiddiq3\SALLM\Evaluation
python run_tests.py
```

### Configuration Options in `run_tests.py`
```python
DEBUG = True                    # Print Docker output
MAX_WORKERS = 4               # Number of parallel workers
RUN_TESTS_ON_GENERATED_CODE = True  # Process JSONL files
TEST_MODE = True              # Only process 1 sample per file (for testing)
MODEL_FILTER = None           # Filter by model: 'gpt', 'gemini', etc.
```

### Example File Path
The script processes files from:
```
Generation/Filtered_Output/dataset_nl_prompt_best_gpt-4o-mini_0.0.jsonl
Generation/Filtered_Output/dataset_nl_prompt_best_gpt-4o-mini_0.2.jsonl
... etc.
```

## Output Files

### Results Location
- **Model Results**: `Evaluation/TestModelsResults/` - Results from GPT/model generated code
- **Dataset Results**: `Evaluation/TestResults/` - Results from original dataset code
- **Temp Files**: `Evaluation/temp/` - Temporary extracted files (cleaned up between runs)
- **Test Files**: `Evaluation/test/` - Test intermediate files

### Output Filename Format
```
Model_{model_name}_{language}_{technique}_{item_id}_results.csv
```

## Notes for Windows Users

1. **Path Separators**: The code now handles both Windows (`\`) and Docker (`/`) path styles
2. **Container Names**: Docker container names have forward slashes removed to avoid Windows issues
3. **Report Directory Names**: Also sanitized to work on Windows
4. **Docker Volume Mounting**: Uses forward slashes internally as required by Docker on Windows

## Testing

To verify the setup is working:
1. Set `TEST_MODE = True` to process only 1 sample per file
2. Set `DEBUG = True` to see Docker output
3. Run: `python run_tests.py`
4. Check `TestModelsResults/` folder for output CSV files

## Troubleshooting

### Docker command not found
- Ensure Docker Desktop is installed
- Add Docker to Windows PATH or restart terminal after installation
- Verify: `docker --version` in PowerShell

### Path-related errors
- Ensure absolute paths are being used
- Check that temp, test, and output folders exist
- Verify GENERATED_CODE_PATH points to valid JSONL files

### No files found to process
- Verify JSONL files exist in `Generation/Filtered_Output/`
- Check MODEL_FILTER isn't filtering out all files
- Ensure test files have `_cwe` in their names (required by the script)

