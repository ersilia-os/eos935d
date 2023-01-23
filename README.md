# MetaTrans: human drug metabolites

Small molecules are metabolized by the liver in what is known as phase I and phase II reactions. Those can lead to reduced drug efficacy and generation of toxic metabolites, causing serious side effects. This model predicts the human metabolites of small molecules using a molecular transformer pr-trained on general chemical reactions and fine tuned to human metabolism. It provides up to 10 metabolites for each input molecule.

## Identifiers

* EOS model ID: `eos935d`
* Slug: `meta-trans`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Generative`
* Output: `Compound`
* Output Type: `String`
* Output Shape: `List`
* Interpretation: A maximum of 10 human metabolites generated from the input molecule

## References

* [Publication](https://pubs.rsc.org/en/content/articlelanding/2020/sc/d0sc02639e#fn1)
* [Source Code](https://github.com/KavrakiLab/MetaTrans)
* Ersilia contributor: [carcablop](https://github.com/carcablop)

## Citation

If you use this model, please cite the [original authors](https://pubs.rsc.org/en/content/articlelanding/2020/sc/d0sc02639e#fn1) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a BSD-3.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!