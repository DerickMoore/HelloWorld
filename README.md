# HelloWorld
First Test GitHub repository

## Overview
This project contains utility functions including a prime number checker and a hello world printer.

## Files
- `helloworld.py` - Main application with `is_prime()` and `dm_hello()` functions
- `dm_func.py` - Additional utility functions
- `test_helloworld.py` - Unit tests for the application
- `.gitignore` - Excludes Python cache files and virtual environments from Git

## Running the Application
To run the main application:
```bash
python helloworld.py
```

## Running Unit Tests
To run all unit tests:
```bash
python -m unittest test_helloworld -v
```

The test suite includes 12 tests covering:
- **is_prime()** function: Tests for edge cases (0, 1, negative numbers), small primes/non-primes, and larger numbers
- **dm_hello()** function: Tests for standard output, empty strings, and special characters

All tests use Python's built-in `unittest` framework and require no additional dependencies.

