OpenAD PaccMann Pretraining
---------------------------

OpenAD is to present PaccMann models for inference and training.

One goal is to make small changes so we can update dependencies:

* python from 3.7 to 3.10
* torch from 1.13.1 to 2.2.1 (latest at time of writing)
* pytoda @ paccmann_datasets from 0.0.1 or 0.1.1 to 1.1.3
* CUDA 11.8 (latest version of cuda-11)

It is being developed on an Amazon AWS g5 host (g5.16xlarge), running Ubuntu.

Where possible, we confine these changes to the training scripts in the 4 packages:

* paccmann_predictor/examples/IC50/train_paccmann.py
* paccmann_omics/examples
* paccmann_chemistry
* paccmann_generator

We add concrete python scripts to run `main` from each of these training scripts with particular
arguments, with the same assumptions as in the original PaccMann^RL documentation:

* Current working directory is the root directory of paccmann_rl.
* The 4 paccmann components are cloned below directory, `code`.
* The data files are downloaded from Box folders shared by the original authors, and are
laid out in directory, `data`.
*

These concrete `do_train_*.py` scripts pass the needed paths to the training scripts.

One tricky piece requiring some special-purpose code is adapting the saved
SMILESLanguage instance loaded from a pickle file. This instance was created with
paccmann_datasets pytoda version 0.0.1 or 0.1.1

Mon Mar 11 2024
Files are set up for training like this:

Showing only 3 levels for clarity:
See how code/ and data/ directories have been set up as in docs of paccmann_rl

Data has been downloaded using instructions in paccmann_rl and paccmann_predictor.

```tree
~/phillipdowney$ tree -L 3
.
└── paccmann_rl
    ├── LICENSE
    ├── README.md
    ├── code
    │   ├── paccmann_datasets tag 1.1.3
    │   └── paccmann_predictor 
    ├── conda.yml
    ├── data
    │   ├── 2128_genes.pkl
    │   ├── README.md
    │   ├── drug_sensitivity
    │   ├── gdsc_transcriptomics_for_conditional_generation.pkl
    │   ├── gene_expression
    │   ├── raw
    │   ├── smiles
    │   ├── smiles_language_chembl_gdsc_ccle.pkl
    │   └── splitted_data
    ├── models
    ├── requirements.txt
    └── run-train_paccmann.sh

11 directories, 9 files
```

---

Showing 4 levels:

```tree
~/phillipdowney$ tree -L 4
.
└── paccmann_rl
    ├── LICENSE
    ├── README.md
    ├── code
    │   ├── paccmann_datasets
    │   │   ├── LICENSE
    │   │   ├── README.md
    │   │   ├── bin
    │   │   ├── conda.yml
    │   │   ├── dev_requirements.txt
    │   │   ├── docs
    │   │   ├── examples
    │   │   ├── pyproject.toml
    │   │   ├── pytoda
    │   │   ├── requirements.txt
    │   │   ├── setup.cfg
    │   │   └── setup.py
    │   └── paccmann_predictor
    │       ├── LICENSE
    │       ├── README.md
    │       ├── assets
    │       ├── examples
    │       ├── models
    │       ├── paccmann_predictor
    │       ├── results
    │       ├── results.csv
    │       ├── run-test_paccmann.sh
    │       ├── run-training-log.txt
    │       ├── setup.py
    │       └── single_pytorch_model
    ├── conda.yml
    ├── data
    │   ├── 2128_genes.pkl
    │   ├── README.md
    │   ├── drug_sensitivity
    │   │   ├── ccle_drug-sensitivity.csv
    │   │   ├── gdsc-cell-line-name_drug-sensitivity.csv
    │   │   └── gdsc-cosmic-id_drug-sensitivity.csv
    │   ├── gdsc_transcriptomics_for_conditional_generation.pkl
    │   ├── gene_expression
    │   │   ├── acc-tcga-rnaseq_gene-expression.csv
    │   │   ├── blca-tcga-rnaseq_gene-expression.csv
    │   │   ├── brca-tcga-rnaseq_gene-expression.csv
    │   │   ├── ccle-rma_gene-expression.csv
    │   │   ├── ccle-rnaseq_gene-expression.csv
    │   │   ├── cesc-tcga-rnaseq_gene-expression.csv
    │   │   ├── chol-tcga-rnaseq_gene-expression.csv
    │   │   ├── coad-tcga-rnaseq_gene-expression.csv
    │   │   ├── coadread-tcga-rnaseq_gene-expression.csv
    │   │   ├── dlbc-tcga-rnaseq_gene-expression.csv
    │   │   ├── esca-tcga-rnaseq_gene-expression.csv
    │   │   ├── gbm-tcga-rnaseq_gene-expression.csv
    │   │   ├── gbmlgg-tcga-rnaseq_gene-expression.csv
    │   │   ├── gdsc-rma_gene-expression.csv
    │   │   ├── gdsc-rnaseq_gene-expression.csv
    │   │   ├── hnsc-tcga-rnaseq_gene-expression.csv
    │   │   ├── kich-tcga-rnaseq_gene-expression.csv
    │   │   ├── kipan-tcga-rnaseq_gene-expression.csv
    │   │   ├── kirc-tcga-rnaseq_gene-expression.csv
    │   │   ├── kirp-tcga-rnaseq_gene-expression.csv
    │   │   ├── lgg-tcga-rnaseq_gene-expression.csv
    │   │   ├── lihc-tcga-rnaseq_gene-expression.csv
    │   │   ├── luad-tcga-rnaseq_gene-expression.csv
    │   │   ├── lusc-tcga-rnaseq_gene-expression.csv
    │   │   ├── ov-tcga-rnaseq_gene-expression.csv
    │   │   ├── paad-tcga-rnaseq_gene-expression.csv
    │   │   ├── pcpg-tcga-rnaseq_gene-expression.csv
    │   │   ├── prad-tcga-rnaseq_gene-expression.csv
    │   │   ├── sarc-tcga-rnaseq_gene-expression.csv
    │   │   ├── skcm-tcga-rnaseq_gene-expression.csv
    │   │   ├── stad-tcga-rnaseq_gene-expression.csv
    │   │   ├── stes-tcga-rnaseq_gene-expression.csv
    │   │   ├── tcga-rma_gene-expression.csv
    │   │   ├── tgct-tcga-rnaseq_gene-expression.csv
    │   │   ├── thca-tcga-rnaseq_gene-expression.csv
    │   │   ├── thym-tcga-rnaseq_gene-expression.csv
    │   │   ├── ucec-tcga-rnaseq_gene-expression.csv
    │   │   ├── ucs-tcga-rnaseq_gene-expression.csv
    │   │   └── uvm-tcga-rnaseq_gene-expression.csv
    │   ├── raw
    │   │   └── gdsc_rma_raw.csv
    │   ├── smiles
    │   │   ├── ccle.smi
    │   │   ├── chembl_22_clean_1576904_sorted_std_final.smi
    │   │   ├── chembl_cleaned.smi
    │   │   └── gdsc.smi
    │   ├── smiles_language_chembl_gdsc_ccle.pkl
    │   └── splitted_data
    │       ├── ccle_ic50_test_fraction_0.1_id_246_seed_42.csv
    │       ├── ccle_ic50_train_fraction_0.9_id_246_seed_42.csv
    │       ├── gdsc_cell_line_ic50_test_fraction_0.1_id_997_seed_42.csv
    │       ├── gdsc_cell_line_ic50_train_fraction_0.9_id_997_seed_42.csv
    │       ├── gdsc_cosmic_cell_line_ic50_test_fraction_10.csv
    │       ├── gdsc_cosmic_cell_line_ic50_train_fraction_90.csv
    │       ├── tcga_rnaseq_test_fraction_0.1_id_242870585127480531622270373503581547167_seed_42.csv
    │       ├── tcga_rnaseq_train_fraction_0.9_id_242870585127480531622270373503581547167_seed_42.csv
    │       ├── test_chembl_22_clean_1576904_sorted_std_final.smi
    │       └── train_chembl_22_clean_1576904_sorted_std_final.smi
    ├── models
    ├── requirements.txt
    └── run-train_paccmann.sh

21 directories, 80 files
```

---

Also needed to change 2 lines of train_paccmann.py:

```diff
-        device=torch.device(params.get("dataset_device", "cpu")),
+        device=None,

-        f"Device for data loader is {train_dataset.device} and for "
+        f"Device for data loader is {getattr(test_dataset, "device", None)} and for
```
