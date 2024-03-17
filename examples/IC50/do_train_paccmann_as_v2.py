"""
Runs in Python an updated, `paccmann_v2` equivalent of the command line
documented at paccmann_rl:
https://github.com/PaccMann/paccmann_rl?tab=readme-ov-file#multimodal-drug-sensitivity-predictor

Here paths have been adjusted to reflect more accurately the paths where the
necessary data files are located, after you copy `splitted_data` into `data`.

Expects the current working directory to be the base of the cloned paccmann_rl
repo, with `code` and `data` directories as documented in paccmann_rl:
https://github.com/PaccMann/paccmann_rl?tab=readme-ov-file#requirements

1. Activate the environment where you have installed the updated Python 3.10,
recent PyTorch, pytoda, and the PaccMann packages.

2. Change into paccmann_rl base directory.

3. Run without arguments:

    $ python ./code/paccmann_predictor/examples/IC50/do_train_paccmann_as_v2.py
"""
import os
import train_paccmann

# Updated from this original from the docs:
# https://github.com/PaccMann/paccmann_rl?tab=readme-ov-file#multimodal-drug-sensitivity-predictor
# $ python ./code/paccmann_predictor/examples/train_paccmann.py \
#     ./data/splitted_data/gdsc_cell_line_ic50_train_fraction_0.9_id_997_seed_42.csv \
#     ./data/splitted_data/gdsc_cell_line_ic50_test_fraction_0.1_id_997_seed_42.csv \
#     ./data/gdsc-rnaseq_gene-expression.csv \
#     ./data/gdsc.smi \
#     ./data/2128_genes.pkl \
#     ./data/smiles_language_chembl_gdsc_ccle.pkl \
#     ./models/ \
#     ./code/paccmann_predictor/examples/example_params.json paccmann

# Environment option to set alternate paths
PACCMANN_DATA = os.getenv("PACCMANN_DATA", "./data")
PACCMANN_CODE = os.getenv("PACCMANN_CODE", "./code")
PACCMANN_MODELS = os.getenv("PACCMANN_MODELS", "./models")
TRAINING_NAME = "paccmann_v2_20240317_1043"

train_sensitivity_filepath = os.path.join(
    PACCMANN_DATA,
    "splitted_data/gdsc_cell_line_ic50_train_fraction_0.9_id_997_seed_42.csv",
)
test_sensitivity_filepath = os.path.join(
    PACCMANN_DATA,
    "splitted_data/gdsc_cell_line_ic50_test_fraction_0.1_id_997_seed_42.csv",
)
gep_filepath = os.path.join(
    PACCMANN_DATA,
    "gene_expression/gdsc-rnaseq_gene-expression.csv",
)
smi_filepath = os.path.join(
    PACCMANN_DATA,
    "smiles/gdsc.smi",
)
gene_filepath = os.path.join(
    PACCMANN_DATA,
    "2128_genes.pkl",
)
smiles_language_filepath = os.path.join(
    PACCMANN_DATA,
    "smiles_language_chembl_gdsc_ccle.pkl",
)
params_filepath = os.path.join(
    PACCMANN_CODE,
    "paccmann_predictor/examples/IC50/paccmann_v2_params.json", 
)

train_paccmann.main(
    train_sensitivity_filepath=train_sensitivity_filepath,
    test_sensitivity_filepath=test_sensitivity_filepath,
    gep_filepath="./data/gene_expression/gdsc-rnaseq_gene-expression.csv",
    smi_filepath="./data/smiles/gdsc.smi",
    gene_filepath="./data/2128_genes.pkl",
    smiles_language_filepath="./data/smiles_language_chembl_gdsc_ccle.pkl",
    model_path=PACCMANN_MODELS,
    params_filepath="./code/paccmann_predictor/examples/IC50/paccmann_v2_params.json",
    training_name=TRAINING_NAME,
)
