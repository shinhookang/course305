# Development Environment

We will utilize a virtual environment for Python 3.11.

For Window users, install WSL2. 

## Install WSL2 

1. Install Windows Terminal from Microsoft Store.

2. WSL2 
Run Termnial in administrator mode.
(Windows + S, search Terminal, Right-click to run in administrator mode.)
Type the following commands:
```
$ wsl —install 
$ wsl --set-default-version 2
```

3. Install Ubuntu Linux from Microsoft Store
ID: kus2025, PASSWD: kus2025

4. Check the WSL version 
```
$ wsl -l -v 
```
If version is 1, then try 
```
$ wsl --set-version Ubuntu 2
$ wsl -l -v 
```

5. Update Ubuntu distribution
```
sudo apt update
sudo apt upgrade
```

## Install Python 3.11

1. Install `Pyenv` and Set up your shell environment for `Pyenv`

For mac users, 
```bash
brew update
brew install pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init - zsh)"' >> ~/.zshrc
source ~/.zshrc
```

For Windows WSL users,
```bash
curl https://pyenv.run | bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
source ~/.zshrc
```

Check **shims** in PATH variable.
```bash
$> echo $PATH
/Users/Shinhoo/.pyenv/shims:/
```

Check available Python version by `pyenv install --list`



2. Install python 3.11.0 by `pyenv install 3.11.0`

(Uninstall python 3.11.0 by `pyenv uninstall 3.11.0`)


3. Use installed Python 3.11.0

Check list of python versions `pyenv versions`

Set python 3.11 locally by `pyenv local 3.11.0`

(Undo `pyenv local --unset`)

Check the prefix of `pyenv`
```bash
$> pyenv prefix
/Users/Shinhoo/.pyenv/versions/3.11.0
```

You can set python 3.11 globally by `pyenv global 3.11.0`

(Undo `pyenv global system`)

 
## Create a virtual environment
Create a virtual environment. `python -m venv .venv`

Activate the virtual environment. `source .venv/bin/activate`

Deactivate the virtual environment. `deactivate`


## Install Python Libraries

* numpy
* scipy
* matplotlib
* ipykernel

```bash
pip install --upgrade pip
pip install numpy scipy matplotlib ipykernel
```
(You can uninstall Python library using `pip uninstall numpy`)

Check the installed Python packages by `pip list`

<!-- ## Reference [PyEnv](https://github.com/pyenv/pyenv) -->
