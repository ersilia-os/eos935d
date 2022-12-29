# Prediction of Drug Metabolites

## Model identifiers
- Slug: <drug-metabolites>
- Ersilia ID: <eos935d>
- Tags: <predict, metabolites, translation>

## Model description

 Model to predict drug metabolites, based on a transformer-based deep learning architecture.
 First, a Transformer model  is pre-trained on a set of chemical reactions (the specifications were based on the Molecular Transformer: https://github.com/pschwllr/MolecularTransformer ). The model is then fitted to a data set of human metabolic transformations. Finally, a final model is created, which is a set of multiple fitted models. The output would be the union of the predictions of each model.
- Input: SMILES
- Output: {sequences of SMILES of the possible metabolites) 
- Model type: (Deep learning, Transformer-based, neural machine translation)
- Mode of training: (Pretrained on a set of chemical reactions- Download the trained models from https://rice.box.com/s/5jeb5pp0a3jjr3jvkakfmck4gi71opo0 ).
## Source code

Cite the source publication

```
@article{metatrans,
  author = {Litsa, Eleni E. and Das, Payel and Kavraki, Lydia E.},
  title = {Prediction of drug metabolites using neural machine translation},
  journal = {Chemical Science},
  year = {2020},
  month = sep,
  publisher = {The Royal Society of Chemistry},
  doi = {10.1039/D0SC02639E},
  url = {http://dx.doi.org/10.1039/D0SC02639E},
  issue = {11},
  pages = {12777-12788}
}
```

- Code: https://github.com/KavrakiLab/MetaTrans
- Checkpoints:https://rice.box.com/s/5jeb5pp0a3jjr3jvkakfmck4gi71opo0

## License

Open Source under the terms of a BSD 3-Clause License.

## History

- The model was downloaded and incorporated on December 28, 2022.
- The original model was modified to process input data from a file with three columns as the Ersilia input file.
  Removed parts of the code so that it would not save images of the metabolite predictions of each Smile.
  Added the path and directory to save the predictions of each fitted model.

## About us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission or [volunteer](https://www.ersilia.io/volunteer) with us!
