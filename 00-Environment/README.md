# Python Development Environment

This guide covers how to set up a Python development environment on **Windows**, **Mac**, and **Linux**, and how to work with **virtual environments** to keep project dependencies isolated.

---

# 1. Install Python

## Windows

Python on Windows is best used through **WSL2 (Windows Subsystem for Linux)**, which gives you a full Linux environment running natively on Windows.

### Step 1 — Install Windows Terminal

Install **Windows Terminal** from the Microsoft Store for a better terminal experience.

### Step 2 — Install WSL2

Open Terminal in **administrator mode** (Windows + S → search "Terminal" → Right-click → Run as administrator) and run:

```
wsl --install
wsl --set-default-version 2
```

### Step 3 — Install Ubuntu

Install **Ubuntu** from the Microsoft Store. When prompted, set up a username and password.

> Example: ID: `kus2024`, Password: `kus2024`

### Step 4 — Verify WSL version

```bash
wsl -l -v
```

If the version shown is `1`, upgrade it:

```bash
wsl --set-version Ubuntu 2
wsl -l -v
```

### Step 5 — Install Python inside WSL2

Update the Ubuntu package list and install Python tools:

```bash
sudo apt update
sudo apt upgrade
sudo apt upgrade python3
sudo apt install python3-pip
sudo apt install python3-venv
python3 -m pip install --upgrade pip
```

Verify the installation:

```bash
python3 --version
```

---

## Mac

### Step 1 — Install Homebrew

[Homebrew](https://brew.sh) is the standard package manager for macOS.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Step 2 — Install Python

```bash
brew install python
```

Verify the installation:

```bash
python3 --version
```

### (Optional) Managing multiple Python versions with pyenv

If you need to switch between Python versions, use **pyenv**.

```bash
brew update
brew install pyenv
```

Set up your shell (for zsh):

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init - zsh)"' >> ~/.zshrc
source ~/.zshrc
```

List available Python versions and install one:

```bash
pyenv install --list
pyenv install 3.11.0
```

Set the Python version for a specific project directory:

```bash
pyenv local 3.11.0    # applies only to the current directory
```

Or set a global default:

```bash
pyenv global 3.11.0   # applies system-wide
```

---

## Linux

On most Linux distributions, Python 3 is already installed. To install or upgrade it manually:

### Debian / Ubuntu

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 -m pip install --upgrade pip
```

### Fedora / RHEL / CentOS

```bash
sudo dnf install python3 python3-pip
```

### Arch Linux

```bash
sudo pacman -S python python-pip
```

Verify the installation:

```bash
python3 --version
pip3 --version
```

---

# 2. Virtual Environments

A **virtual environment** is an isolated Python environment for a project. It keeps each project's packages separate from the system Python and from other projects.

```
project/
├── .venv/          ← virtual environment (not committed to git)
├── main.py
└── requirements.txt
```

## Create a virtual environment

Inside your project directory, run:

```bash
python3 -m venv .venv
```

This creates a `.venv` folder containing a private copy of Python and pip.

## Activate the virtual environment

| Platform | Command |
|---|---|
| Mac / Linux | `source .venv/bin/activate` |
| Windows (WSL2) | `source .venv/bin/activate` |
| Windows (CMD) | `.venv\Scripts\activate.bat` |
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |

After activation, your prompt changes to show `(.venv)`, and `python` / `pip` now refer to the versions inside the virtual environment:

```bash
(.venv) $ python --version
(.venv) $ pip list
```

## Install packages

```bash
pip install numpy scipy matplotlib jupyterlab seaborn 
```

## Save and restore dependencies

Save the current environment's packages to a file:

```bash
pip freeze > requirements.txt
```

Restore them in a new environment:

```bash
pip install -r requirements.txt
```

## Deactivate the virtual environment

```bash
deactivate
```

> **Best practice:** Always activate your virtual environment before working on a project, and never install packages globally with `sudo pip`.

---

<!-- # 3. SSH Access to a Remote Server

## Enable SSH on the server

```bash
sudo apt update
sudo apt install openssh-server
sudo systemctl enable ssh
sudo systemctl start ssh
sudo ufw allow ssh
```

For older systems: `sudo service ssh restart`

## Connect to the server

```bash
ssh <username>@<ip-address>
```

## Key-based (passwordless) login

1. Generate an SSH key on your local machine:
   ```bash
   ssh-keygen -t ed25519
   ```
2. Copy the public key to the server:
   ```bash
   ssh-copy-id <username>@<ip-address>
   ```

## Change the default SSH port

Edit `/etc/ssh/sshd_config` and change `Port 22` to a custom port number:

```bash
sudo nano /etc/ssh/sshd_config
```

Restart SSH after saving:

```bash
sudo systemctl restart ssh
``` -->
