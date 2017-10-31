# RAMP starting kit on the Kaggle Seguro dataset

Authors: Balazs Kegl

[![Build Status](https://travis-ci.org/ramp-kits/kaggle_seguro.svg?branch=master)](https://travis-ci.org/ramp-kits/kaggle_seguro)

Go to [`ramp-worflow`](https://github.com/paris-saclay-cds/ramp-workflow/wiki) for more help on the [RAMP](http:www.ramp.studio) ecosystem.

Get started on this RAMP with the [dedicated notebook](kaggle_seguro_starting_kit.ipynb).

This is the RAMP starting kit for the  [Kaggle data challenge](https://www.kaggle.com/c/porto-seguro-safe-driver-prediction) on predicting the probability that a driver will initiate an auto insurance claim in the next year. You can use it to make submissions that you can submit both at Kaggle and at the [RAMP we built](http://www.ramp.studio/problems/kaggle_seguro)) for forming a team that collaborates and submits together at Kaggle.

## Setting up the starting kit

First install ramp-workflow (rampwf). For now you need to pull from a temporary branch to install the latest tools you will need for, e.g., outputting predictions ready made for Kaggle. 
```
git clone https://github.com/paris-saclay-cds/ramp-workflow.git
cd ramp-workflow
git checkout cv_bagging
python setup.py install

Second, install this kit
```
git https://github.com/ramp-kits/kaggle_seguro.git
cd kaggle_seguro
pip install -r requirements.txt
```
This will create the following arborescence
```
kaggle_seguro/
├── data
│   ├── sample_submission.csv
│   ├── test.csv
│   └── train.csv
├── submissions
│   ├── starting_kit
│   │   ├── classifier.py
│   │   └── feature_extractor.py
├── kaggle_seguro_starting_kit.ipynb
├── README.md
├── mock_data.py
├── problem.py
└── requirements.txt
```
Execute
```
ramp_test_submission --quick-test
```
to test `submissions/starting_kit/feature_extractor.py` and `submissions/starting_kit/classifier.py` against the mock data in `data/`. If you want to test the starting kit on the official Kaggle data, sign up to the [Kaggle challenge](https://www.kaggle.com/c/porto-seguro-safe-driver-prediction), download `train.7z` and `test.7z`, unzip them and place them in `kaggle_data/`. If you want to use the starting kit to generate output in the right Kaggle submission format, you will also need to download `sample_submission.7z`, unzip it, and place it in `kaggle_data/`. Once the data is in place, execute
```
ramp_test_submission
```
If it runs and print training and test errors on each fold, then your setup is complete.

Please refer to the corresponding section in the [notebook](kaggle_seguro_starting_kit.ipynb) for more information about submitting to RAMP and to Kaggle.
