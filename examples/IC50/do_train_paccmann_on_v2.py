"""
Runs in Python an updated, `paccmann_v2` equivalent of the command line
documented at paccmann_rl:
https://github.com/PaccMann/paccmann_rl?tab=readme-ov-file#multimodal-drug-sensitivity-predictor

Paths have been adjusted to reflect more accurately the paths where the
necessary data files are located, after you copy `splitted_data` into `data`.

Expects the current working directory to be the base of the cloned paccmann_rl
repo, with `code` and `data` directories as documented in paccmann_rl:
https://github.com/PaccMann/paccmann_rl?tab=readme-ov-file#requirements

1. Activate the environment where you have installed the updated Python 3.10,
recent PyTorch, pytoda, and the PaccMann packages.

2. Change into paccmann_rl base directory.

3. Run without arguments:

    $ python ./code/paccmann_predictor/examples/IC50/do_train_paccmann_on_v2.py

"""
import train_paccmann

train_paccmann.main(
    train_sensitivity_filepath="./data/splitted_data/gdsc_cell_line_ic50_train_fraction_0.9_id_997_seed_42.csv",
    test_sensitivity_filepath="./data/splitted_data/gdsc_cell_line_ic50_test_fraction_0.1_id_997_seed_42.csv",
    gep_filepath="./data/gene_expression/gdsc-rnaseq_gene-expression.csv",
    smi_filepath="./data/smiles/gdsc.smi",
    gene_filepath="./data/2128_genes.pkl",
    smiles_language_filepath="./data/smiles_language_chembl_gdsc_ccle.pkl",
    model_path="./models/",
    params_filepath="./code/paccmann_predictor/examples/IC50/paccmann_v2_params.json",
    training_name="paccmann_v2",
)
