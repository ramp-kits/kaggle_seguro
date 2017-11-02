# RAMP starting kit on the Kaggle Seguro dataset

Authors: Balazs Kegl

[![Build Status](https://travis-ci.org/ramp-kits/kaggle_seguro.svg?branch=master)](https://travis-ci.org/ramp-kits/kaggle_seguro)

This is the RAMP starting kit for the [Kaggle data challenge](https://www.kaggle.com/c/porto-seguro-safe-driver-prediction) on predicting the probability that a driver will initiate an auto insurance claim in the next year. You can use it to make submissions that you can submit both at Kaggle and at the [RAMP we built](http://www.ramp.studio/problems/kaggle_seguro) for **forming a team that collaborates and submits together at Kaggle**.

### Quick start

```
pip install git+https://github.com/paris-saclay-cds/ramp-workflow.git
git https://github.com/ramp-kits/kaggle_seguro.git
cd kaggle_seguro
pip install -r requirements.txt
ramp_test_submission --quick-test
```
Go to [`ramp-workflow`](https://github.com/paris-saclay-cds/ramp-workflow/wiki) for more help on the [RAMP](http:www.ramp.studio) ecosystem.

Get started on this RAMP with the [dedicated notebook](kaggle_seguro_starting_kit.ipynb).

## Rules

This is the starting kit of a special [RAMP](http://www.ramp.studio/events/kaggle_seguro) whose goal is to participate in the Kaggle challenge as a team. This means that you need to observe certain rules **before signing up to the [RAMP](http://www.ramp.studio/events/kaggle_seguro)**. 
1. You need to have a **valid Kaggle account**.
2. You need to officially sign up to the [Kaggle challenge](https://www.kaggle.com/c/porto-seguro-safe-driver-prediction), which naturally means that you accept all the [Kaggle rules](https://www.kaggle.com/c/porto-seguro-safe-driver-prediction/rules).
3. You will have **not made more than five submissions** at the time you would like to join the RAMP team. This is a rule assuring that the number of submissions of the RAMP team will not exceed 310 which is the total number of submissions any team can have (5 per day for 62 days). We will **retain the right to make exceptions** to this rule in case you have a reasonably low number of submissions and a score close to the top score.
4. You will have **joined the "RAMP Seguro" team on the Kaggle challenge**. You can ask for joining by posting your kaggle username at the [RAMP slack](https://ramp-studio.slack.com/shared_invite/MTg1NDUxNDAyNDk2LTE0OTUzOTcwMDQtMThlOWY1NWU0Mg), channel `#kaggle_seguro`. 

RAMP sign-ups will naturally close at the team merger deadline on November 22. We retain the right to close the sign-ups at an earlier date. The RAMP will run in **competitive mode until November 20 at 20h** and in collaborative (open code) mode between November 20 at 20h and the submission deadline. The RAMP team will make **two submissions**, a first one **one day before the deadline**, and a second one **two hours before the deadline**. 

### Incentives

In case the RAMP team wins one of the money prizes, **50% will go to the RAMP organizers** (we will recycle it as money prize for future RAMPs), 25% will be shared proportionally to the **contributions to the combined (ensemble) score (jumps, starting at the single submission called "xgboost baseline" that the RAMP organizers will submit in the beginning of the RAMP)**, and 25% will be shared according to the **influence** of the submitters, computed using the non-self credits participants give to submissions of other participants after each submission.

There will not be a strict limit on resource use but make an effort to keep your total training time below 50 hours. We retain the right to disqualify your submissions if they take too much time to train.

## Setting up the starting kit

First install `ramp-workflow` (`rampwf`). 
```
pip install git+https://github.com/paris-saclay-cds/ramp-workflow.git
```
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
├── README.md
├── kaggle_seguro_starting_kit.ipynb
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

Please refer to the corresponding sections in the [notebook](kaggle_seguro_starting_kit.ipynb) for more information about submitting to RAMP and to Kaggle.
