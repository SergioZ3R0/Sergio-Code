# `pythonRansomware` - Ransomware Simulation Scripts
AÑADIR ROBO DE LOS DATAOS
This directory contains Python scripts for a ransomware simulation. The scripts encrypt all non-critical system files in a specified directory and delete the original files. They also provide a mechanism to restore the files from the encrypted versions.

## Table of Contents

- [Scripts](#scripts)
- [Usage](#usage)
- [Disclaimer](#disclaimer)

## Scripts

- `darthvader.py`: This script encrypts all non-critical system files in the current directory and sends the encryption key to a specified host.
- `decrypt.py`: This script decrypts all files in the current directory using a provided encryption key.
- `window.py`: Shows a simple windos with some information to make the victim pay the rescue
- `spread.py`: Search and finds some services vulnerable to spread the Randsomware'
- `auto_run`: An autorun writen on c++ compiled to download and execute darthvader.py
- `auto_run.cpp`: C++ code to compile the autorun
- `window.py`: Shows a simple windos with some information to make the victim pay the rescue
- `spread.py`: Search and finds some services vulnerable to spread the Randsomware'

## Usage

### Encrypting Files

To encrypt the files in the current directory, run the `darthvader.py` script:

python3 darthvader.py


This will encrypt all non-critical system files in the current directory and send the encryption key to the host specified in the script.

### Restoring Files

To restore the files from the encrypted versions, run the `decrypt.py` script:

python3 decrypt.py

### Window Display

python3 window.py


This will decrypt all files in the current directory using the encryption key stored in `key.key`.

### Spreading the malware

Search and finds some services vulnerable to spread the Randsomware

spread.py

### Autorun to infect

An autorun writen on c++ compiled to download and execute darthvader.py

auto_run

auto_run.cpp

### Stealing data

Steal data from the victim

steal.py

## Disclaimer

These scripts are simulations and should not be used for malicious purposes. Always ensure you have a backup of your files before running the scripts.

Do not download compiled auto_run and execute it it may run darthvader.py and encrypt your files
