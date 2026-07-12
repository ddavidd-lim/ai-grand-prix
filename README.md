# AI Grand Prix (DABJAK4)
Drone control loop implementation for the Anduril AI Grand Prix.

## Setup
Download the competition simulator package from the competition dashboard.

### Python Environment Setup

Initialize virtual environment

```sh
python -m venv .venv
python -m .\.venv\Scripts\activate # Activate virtual environment
```

Install packages

```sh
pip install -r requirements.txt
pip install -e . # Download code as modules
```

Run control loop

```sh
python .\src\main.py
```

### Simulator setup

The simulator is available from the `AIGP_3364.zip` folder.

Extract this file and run `FlightSim.exe`.

To test the control loop, run the Python code concurrently with `FlightSim.exe`.
