# KNEEL: Hourglass Networks for Knee Anatomical Landmark Localization

(c) Aleksei Tiulpin, University of Oulu, 2019

## About
The repository includes the codes for training and testing, 
annotations for the OAI dataset and also the pre-trained models.

## How to install and run
### Preparing the training data
We provide the script and the annotations for creating the cropped ROIs from the original DICOM images. The annotations are stored in the file `annotations/bf_landmarks_1_0.3.csv`. The script for creating the high cost and the low cost datasets from the raw DICOM data are stored in `scripts/data_stuff/create_datasets_from_via.py`. Follow the arguments to better understand what it does.

### Reproducing the experiments from the paper
All the experiments done in the paper were made with PyTorch 1.0.0 and anaconda.
To run the experiments, simply copy the content of the folder `hc_experiments` into `hc_experiments_todo`. Set up the necessary environment variables in the file `run_experiments.sh` and then run this script. The code is written to leverage all the available GPU reseource running 1 experiment per card.

## Inference on your data
Follow the script `scripts/test_okoa_maknee.py` to see how to do the inference. More detailed description and a Docker image are coming soon.

## License
If you use the annotations from this work, you must cite the following paper

```
@article{tiulpin2019kneel,
  title={KNEEL: Knee Anatomical Landmark Localization Using Hourglass Networks},
  author={Tiulpin, Aleksei and Melekhov, Iaroslav and Saarakkala, Simo},
  journal={arXiv preprint arXiv:1907.12237},
  year={2019}
}
```

The codes and the pre-trained models are not available for any commercial use 
including research for commercial purposes.
