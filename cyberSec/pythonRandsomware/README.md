# `pythonRansomware` - Ransomware Simulation Scripts

This directory contains Python scripts for a ransomware simulation. The scripts encrypt all non-critical system files in a specified directory and delete the original files. They also provide a mechanism to restore the files from the encrypted versions.

## Table of Contents

- [Scripts](#scripts)
- [Usage](#usage)
- [Disclaimer](#disclaimer)

## Scripts

- `voldemort.py`: This script encrypts all non-critical system files in the current directory and sends the encryption key to a specified host.
- `decrypt.py`: This script decrypts all files in the current directory using a provided encryption key.

## Usage

### Encrypting Files

To encrypt the files in the current directory, run the `voldemort.py` script:

```bash
python3 voldemort.pyA

This will encrypt all non-critical system files in the current directory and send the encryption key to the host specified in the script.  
Restoring Files

To restore the files from the encrypted versions, run the decrypt.py script:

python3 decrypt.py

This will decrypt all files in the current directory using the encryption key stored in key.key.  
Disclaimer

These scripts are simulations and should not be used for malicious purposes. Always ensure you have a backup of your files before running the scripts.