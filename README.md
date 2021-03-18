# Popularity Bias in False-Positive Metrics for Recommender Systems Evaluation 

This journal paper comprehensively addresses the effect of popularity in false-positive metric measurements in the evaluation of recommender systems.  In doing so, this work extends another work by the same authors, accepted for publication at [SIGIR 2020](https://github.com/elikary/sigir2020)

##### Citation of this work
> E. Mena-Maldonado, R. Cañamares, [P. Castells](http://ir.ii.uam.es/castells), Y. Ren and [M.Sanderson](http://marksanderson.org). 2021. Popularity Bias in False-Positive Metrics for Recommender Systems Evaluation. Transaction On Information Systems (TOIS).

Paper DOI (https://doi.org/10.1145/3452740)
TOIS PAPER: [TOIS2021 paper](https://github.com/elikary/tois2021/blob/main/paper/TOIS_paper_on_false_positive_metrics.pdf)

## Sotware Required
This project contains two modules:
- **Recommendation:** we used (an edited version) of Librec 2.0.0 library to run the algorithms of our experiments (See [librec-2.0.0](https://github.com/elikary/tois2021/tree/main/librec-2.0.0) folder)
- **Evaluation:** we created some scripts in Python to carry out evaluation (See [FP_metrics](https://github.com/elikary/tois2021/tree/main/FP_metrics) folder)

We have included instructions on how to run each module, please refer to each folder for more information.

## Datasets 
For convinience, we have uploaded binarized versions of the datasets used for all the experiments presented in the paper.  Please see the folder  [`tois2021/librec-2.0.0/data`](https://github.com/elikary/tois2021/tree/main/tois2021/librec-2.0.0/data) 
|Dataset| Train|Test|
|-------|------|----|
|MOVIELENS 1M| Observed |Observed|
|CM100K |Observed|Observed and True|
|CM100K SYNTHETIC|Observed|Observed and True|
|YAHOO! R3 |Observed|Observed and True|

We run evaluation under 5-fold cross validation except in Movielens 1M time split.

## OS support
The code was tested on Linux

        NAME="Red Hat Enterprise Linux Server"
        VERSION="7.7 (Maipo)"
        
Can possibly run on OSX however this has not been tested yet.











