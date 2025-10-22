# MetaTrans: human drug metabolites

Small molecules are metabolized by the liver in what is known as phase I and phase II reactions. Those can lead to reduced drug efficacy and generation of toxic metabolites, causing serious side effects. This model predicts the human metabolites of small molecules using a molecular transformer pr-trained on general chemical reactions and fine tuned to human metabolism. It provides up to 10 metabolites for each input molecule.

This model was incorporated on 2022-12-16.


## Information
### Identifiers
- **Ersilia Identifier:** `eos935d`
- **Slug:** `meta-trans`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Any`
- **Tags:** `Metabolism`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `15`
- **Output Consistency:** `Fixed`
- **Interpretation:** A maximum of 15 human metabolites generated from the input molecule

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| metabolite_00 | string |  | Metabolite at index 0 of the source molecule |
| metabolite_01 | string |  | Metabolite at index 1 of the source molecule |
| metabolite_02 | string |  | Metabolite at index 2 of the source molecule |
| metabolite_03 | string |  | Metabolite at index 3 of the source molecule |
| metabolite_04 | string |  | Metabolite at index 4 of the source molecule |
| metabolite_05 | string |  | Metabolite at index 5 of the source molecule |
| metabolite_06 | string |  | Metabolite at index 6 of the source molecule |
| metabolite_07 | string |  | Metabolite at index 7 of the source molecule |
| metabolite_08 | string |  | Metabolite at index 8 of the source molecule |
| metabolite_09 | string |  | Metabolite at index 9 of the source molecule |

_10 of 15 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos935d](https://hub.docker.com/r/ersiliaos/eos935d)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos935d.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos935d.zip)

### Resource Consumption
- **Model Size (Mb):** `1294`
- **Environment Size (Mb):** `2049`


### References
- **Source Code**: [https://github.com/KavrakiLab/MetaTrans](https://github.com/KavrakiLab/MetaTrans)
- **Publication**: [https://pubs.rsc.org/en/content/articlelanding/2020/sc/d0sc02639e#fn1](https://pubs.rsc.org/en/content/articlelanding/2020/sc/d0sc02639e#fn1)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2020`
- **Ersilia Contributor:** [carcablop](https://github.com/carcablop)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [BSD-3-Clause](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos935d
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos935d
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
