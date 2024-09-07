'''

Script that runs the training of the deep learning model for the task of
'Predictive Data Analysis' in the COESA/MERSI data set

Author: Christian Herdtweck
Copyright 2020 Christian Herdtweck
Institute for Dynamics
Dortmund University

------------------------------
CommandLine:
    python run_training_cpa.py
    -v for visual output of console outputs. The console outputs are send to stdout. An log file is created to record the console outputs.
    -h --help   show this help message and exit
    --trial=<int> select trial number (set to '0,1,2,3,...') 
    
Input:
    The system command line is callied with the option --trial <int>.
    The data set in the folder 'DATASETS' is loaded, and the COESA/MERSI
    tiles are used with a constant bandpass and constant baseline.

    python run_training_cpa.py --help
    python run_training_cpa.py -h -t=0 -v

    python run_training_cpa.py -d