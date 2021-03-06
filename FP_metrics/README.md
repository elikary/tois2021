## Evaluation
Please note that this step should be done after [Recommendation](https://github.com/elikary/tois2021/tree/main/librec-2.0.0)

To carry out evaluation with precision, anti-precision, recall and fallout on all datasets run:

    $ cd tois2021/FP_metrics/scripts
    $ python main_prec.py 

After the main script runs, you will see the results per each fold in `~/tois2020/FP_metrics/evaluation/` as `<dataset-name>/<dataset-name_fold$i_prec.csv>`. 

![](https://github.com/elikary/tois2021/blob/main/images/folds.png)

Next, to compute the folds average per each dataset run:

    $ python cross_validation.py prec

The suffix/parameter `prec` denotes evaluation with `precision, anti-precision, recall and fallout`.  
Others are available:
- for `MRR` and `anti-MRR`, use `mrr`
- for `nDCG` and `nDCL`, use `ndcg`

The results will be saved in `FP_metrics/evaluation/` as `<dataset-name>/<dataset-name_k_prec.csv>`. For instance `FP_metrics/evaluation/cm100k_observed/cm100k_observed_10_prec.csv`. 

![](https://github.com/elikary/tois2021/blob/main/images/cv.png)
### Visualize Results

Please click on the links below to see the graphs in Jupyter notebooks. You will be redirected to Jupyter nbviewer

- [Figure 1](https://nbviewer.jupyter.org/github/elikary/tois2021/blob/main/FP_metrics/visualization/Figure%201.ipynb)
- [Figure 9](https://nbviewer.jupyter.org/github/elikary/tois2021/blob/main/FP_metrics/visualization/Figure%209.ipynb)
- [Figure 14](https://nbviewer.jupyter.org/github/elikary/tois2021/blob/main/FP_metrics/visualization/Figure%2014.ipynb)
- [Figure 17](https://nbviewer.jupyter.org/github/elikary/tois2021/blob/main/FP_metrics/visualization/Figure%2017.ipynb)
     

### System Requirements

The recommended way to setup a working python environment is to use Anaconda distribution https://www.continuum.io/downloads.
Here is also a list of the required packages:

- Python 3.7.1 
- Pandas
- Numpy
- Scipy
- Matplotlib
- Jupyter Notebook