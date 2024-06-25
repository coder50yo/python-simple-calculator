# Calculator Python Project

This is a simple Python calculator app that performs basic arithmetic operations: addition, subtraction, multiplication, and division.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setting Up the Project](#setting-up-the-project)
- [Running the Calculator](#running-the-calculator)
- [Running the Tests](#running-the-tests)
- [Explanation of the Code](#explanation-of-the-code)
- [Using `.gitignore`](#using-gitignore)
- [Additional Resources](#additional-resources)

## Prerequisites

- [Python](https://www.python.org/downloads/) installed on your system
- [Git](https://git-scm.com/downloads) installed on your system

## Project Structure

The project has the following structure:

```
calculator/
│
├── .gitignore
├── calculator.py
├── test_calculator.py
└── README.md
```

- `calculator.py`: The main Python script that implements the calculator functionality.
- `test_calculator.py`: Unit tests for the calculator functions.
- `.gitignore`: A file specifying which files and directories to ignore in the Git repository.
- `README.md`: A comprehensive tutorial on how to set up and run the calculator project.

## Setting Up the Project

1. **Clone the Repository**

   First, clone the repository to your local machine. Open your terminal and run the following command:

   ```sh
   git clone https://github.com/coder50yo/python-simple-calculator.git
   ```

2. **Navigate to the Project Directory**

   Change into the project directory:

   ```sh
   cd calculator
   ```

## Running the Calculator

To run the calculator, execute the following command in your terminal:

```sh
python3 calculator.py
```

Follow the prompts to choose an operation and enter numbers to perform the calculation.

## Running the Tests

To run the unit tests for the calculator functions, execute the following command in your terminal:

```sh
python3 -m unittest test_calculator.py
```

You should see output indicating that the tests passed.

## Explanation of the Code

### `calculator.py`

The `calculator.py` script defines functions for basic arithmetic operations: `add()`, `subtract()`, `multiply()`, and `divide()`. The script also handles user input to select an operation and input numbers for calculation.

### `test_calculator.py`

The `test_calculator.py` script contains unit tests for each arithmetic operation function (`add()`, `subtract()`, `multiply()`, `divide()`). It uses the `unittest` framework to assert expected results against actual function outputs.

## Using `.gitignore`

The `.gitignore` file specifies files and directories that Git should ignore, such as temporary files, build artifacts, and environment-specific directories.

Here are some common entries in the `.gitignore` file:

- `__pycache__/`: Python's bytecode cache directory
- `*.pyc`: Compiled Python files
- `venv/`, `env/`: Virtual environment directories

## Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Git Official Documentation](https://git-scm.com/doc)
- [unittest Documentation](https://docs.python.org/3/library/unittest.html)