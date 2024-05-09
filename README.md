### dbSNP2NCBI
#### Prequest: Installation of Conda 3

1. Run installation Script
./installation.sh

2. Run Script

    python dbSNP.py -h

    usage: ezSNP: Read-in a list of the SNP, output MAFs [-h] Input_csv Pause_Timer

    Query the SNP from NCBI server

    positional arguments:
      Input_csv    Input SNP list (in csv format)
      Pause_Timer  An pause timer to avoid server overload, unit="s"

    options:
      -h, --help   show this help message and exit

Bo Wang Ph.D., https://github.com/pop3www/dbSNP2NCBI