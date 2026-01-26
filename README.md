# Not A Robot Solver

This project contains a Python script (`robot.py`) that automates solving the "Not A Robot" challenge found at [neal.fun/not-a-robot](https://neal.fun/not-a-robot/). It uses Selenium to interact with the web page and complete the various levels of the challenge.

## Files

- `robot.py`: The main script that implements the automation logic.
- `single.py`: Test automation of a single level

## Setup

1. Install Python (if not already installed).
2. Install the required Python packages:
   ```bash
   pip install selenium
   ```
3. Download and set up a web driver (e.g., ChromeDriver) compatible with your browser and add it to your system's PATH.

## Usage

To run the solver, execute the `robot.py` script:

```bash
python robot.py
```

The script will open a Chrome browser, navigate to the "Not A Robot" challenge, and attempt to solve it automatically.