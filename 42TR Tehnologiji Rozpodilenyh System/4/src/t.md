$ mpiexec -n 1 python 1.py
Proceses amount: 1
Total sum: 146.733741072558
Running time (Tp): 24.6048 sec
Scatter time: 0.000619 sec

$ mpiexec -n 2 python 1.py
Proceses amount: 2
Total sum: -151.31365322656524
Running time (Tp): 12.5789 sec
Scatter time: 0.009543 sec

$ mpiexec -n 3 python 1.py
Proceses amount: 3
Total sum: -314.8372543611528
Running time (Tp): 8.4814 sec
Scatter time: 0.001679 sec

$ mpiexec -n 4 python 1.py
Proceses amount: 4
Total sum: -363.7585435844192
Running time (Tp): 6.6128 sec
Scatter time: 0.008873 sec
