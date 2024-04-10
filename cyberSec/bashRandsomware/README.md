**randsomware.sh Script Summary**


The randsomware.sh script is a ransomware simulation that encrypts all non-critical system files in a specified directory and deletes the original files. It also provides a mechanism to restore the files from the encrypted versions.  

**How to Use**

The script provides several command-line options:  

-h or --help: Displays help information.

-g or --generate: Generates a new encryption key.

-e or --encrypt: Encrypts the files in the specified directory.

-r or --restore: Restores the files from the encrypted versions.

Generating a Key

To generate a new encryption key, run the script with the -g or --generate option:

./randsomware.sh -g

This will create a new key and store it in a file named key.txt in the home directory.

Encrypting Files

To encrypt the files in the specified directory, run the script with the -e or --encrypt option:

./randsomware.sh -e

This will encrypt all non-critical system files in the directory specified by the DIR variable in the script, and delete the original files.

Restoring Files

To restore the files from the encrypted versions, run the script with the -r or --restore option:

./randsomware.sh -r

You will be prompted to enter the password. If the entered password's SHA256 hash matches the PASSWORD_HASH variable in the script, the files will be decrypted and the encrypted versions will be deleted.

**Important Note**

This script is a simulation and should not be used for malicious purposes. Always ensure you have a backup of your files before running the script.

