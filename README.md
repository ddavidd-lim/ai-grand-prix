# AI Grand Prix (DABJAK4)

## Setup

### Prerequisites

- Python
- WSL
- PX4
- Gazebo
- MavSDK
  
### [WSL Installation](https://docs.px4.io/main/en/dev_setup/dev_env_windows_wsl#installation)

Install Ubuntu distribution

```sh
wsl --install -d Ubuntu-22.04
```

Open WSL Terminal

```sh
wsl -d <distribution_name>              # Can use 'wsl' for default distribution
```

> [!TIP]
> You can set up a default distribution to easily open a terminal with 'wsl'
>
> ```sh
>wsl --list                              # Browse installed distributions
>wsl --set-default <distribution_name>   # Set default distribution
>wsl                                     # Open WSL Terminal for default distribution
> ```

### [PX4 Toolchain Installation](https://docs.px4.io/main/en/dev_setup/dev_env_windows_wsl#install-px4-toolchain)

Go to home folder of WSL, clone, run installer script

```sh
cd ~
git clone https://github.com/PX4/PX4-Autopilot.git --recursive
bash ./PX4-Autopilot/Tools/setup/ubuntu.sh
```

Restart the "WSL computer" after the script completes (exit the shell, shutdown WSL, and restart WSL):

```sh
exit
wsl --shutdown
wsl
```

Go to PX4-Autopilot directory again

```sh
cd ~/PX4-Autopilot
```

Build PX4 SITL target and test environment

```sh
make px4_sitl
```

### [Gazebo](https://docs.px4.io/main/en/dev_setup/dev_env_windows_wsl#install-px4-toolchain)

Run Simulation with drone

```sh
make px4_sitl gz_x500_mono_cam
```

> If you get a `ninja: error: unknown target 'gz_x500_mono_cam'`, try `make distclean`

## Python Environment Setup

Initialize virtual environment

```sh
python -m venv .venv
```

Activate environment and install packages

```sh
pip install -r requirements.txt
pip install -e . # Download code as modules
```

Run example

```sh
python .\scripts\takeoff_and_landing.py
```
