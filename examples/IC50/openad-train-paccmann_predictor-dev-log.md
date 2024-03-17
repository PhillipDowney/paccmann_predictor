Developer notes on virtual (conda) env, `openad-train`, paccmann_predictor

Fri Mar 8 2024 Dean Elzinga

What I did was create a virtual (conda) env with almost only python:
dependencies:
  - python>=3.9,<3.11
  - pytest=8.0.2
  - pip

conda activate openad-train

Straight from the PyTorch homepage installation instructions, for constraints:

* CUDA 11.8

* Python 3.10 and pip for installation
```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

Then, from ~/Open-AD-Model-Service/openad-model-training/gt4sd_paccmann,
pip install --dry-run .
# inspect what will be installed... looks good
pip install .
# pip install ~/Open-AD-Model-Service/openad-model-training/gt4sd_paccmann

conda is doing just the virtual environment and setup of the python version in this case.
https://medium.com/@silvinohenriqueteixeiramalta/conda-and-poetry-a-harmonious-fusion-8116895b6380


Mon Mar 11 2024 Dean Elzinga

Several changes required to paccmann_predictor/examples/train_paccmann.py
arising from Python update from 3.7 to 3.10 and PyTorch from 1.7 or 1.13 to 2.2 .

### Error

Traceback (most recent call last):
  File "/home/deanelzinga/phillipdowney/paccmann_rl/./code/paccmann_predictor/examples/IC50/train_paccmann.py", line 343, in <module>
    main(
  File "/home/deanelzinga/phillipdowney/paccmann_rl/./code/paccmann_predictor/examples/IC50/train_paccmann.py", line 313, in main
    if test_loss_a < min_loss:
TypeError: '<' not supported between instances of 'float' and 'str'

### Fix

Surround values with cast, `float()`

Continued in this way, fixing error after error.
