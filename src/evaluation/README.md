# Script for evaluating results
This directory contains evaluation scripts for the contest and the evaluation method for users of the OpenROAD Python API. The evaluation penalties are set to 1 for this sample evaluation script. All penalties are subject to change during the alpha submission, beta submission, and final evaluation stages. The run-time penalty is not included in this sample evaluation script.


## Run evaluation
(Make sure you have OpenROAD built locally)
Run the following command to check the correctness of the resynthesis result and get the sample score:
- Add the name of the corresponding benchmark you want to evaluate with the "-d" flag
```
../../OpenROAD/build/src/openroad -python OpenROAD_flow.py -d <The name of the benchmark>
```
