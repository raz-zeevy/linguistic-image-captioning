# linguistic-image-captioning

## TODO
1. Change the parse_coco_composplit to receive the path's as parameters
2. Change the prediction to be entiryly based on the trained model  and not 
   using the clip for initial encoding.
3. **THE MOST UPDATED VERSION OF linguist_tokenizer.py is in COMPO!!!!**
## Overview

**This project was executed by the HUJI University NLP lab of prop. Omri 
Abend and the guidence of Uri berger.**

**Author: Raz Zeevy**

## Introduction


## Project Structure

The project consists of the following key components:
### Prepare Data - Clip
- *Parse the captions with labels to tagged annotations(`parse_captions.py`):*

### Preprocess Data - Clip
- *Annotations (`data/coco/annotations/`):*

| Test    | Control      | 
|---------|--------------|
| `train_captions.py` | `tagged_train_captions.py`|

- *Image Data (`data/coco/train2014.py`):*
- *Splits dataset .jsons files (`dataset_splits.dataset_splits_#.json`)*: the
- *the bash script (`extract_compo.sh`)*: the
1. **Activate the enviroment**
   ```bash
   source venv/bin/activate.csh
   ```
2. **Run the parsing script for the datasets (`parse_coco_composplit.py`):**
   ```bash
   venv/bin/python parse_coco_composplit.py
   ```
   The output of the preprocess is a ..._train.pkl file and a ..._train_tokens.
   pkl 
   for each of the special splits and for the control
   
### Train Model - Clip

1. **Main Train Script (`train.py`):** 5 models overall are trained :
   - 4 models for each customized split
   - control model
   - (by default created in /compo/)
2. **Tokenizer script (`linguistic_tokenizer.py`):** the tokenizer is created
   during the training and saved in the same directory as the model.

### Evaluate a single photo - Clip

1. **evaluate for one photo (`eval.py`):** the script receives a path to a
   photo and a path to a model and returns the predicted caption.
2. **the Predict class script (`predict.py`):** the class for a predictor
    object, which receives a path to a model (it is assumed that the 
    tokenizer is in the same directory) and contains the "predict" method.

## Evaluate Model - CompoSplit
- *Annotations (`data/coco/annotations/`):*
- *Image Data (`data/coco/train2014.py`):*
- *Splits dataset .jsons files (`dataset_splits.dataset_splits_#.json`)*: the

1. ** (`eval_compo.py`):** the script generates captions for the test set 
   and outputs the results to a .json file.

## Analyze Results - coco-caption

1. ** Evaluate Metrics(`eval_coco_metrics.py):** the script receives a path to
   a .json file and outputs the metrics for the captions in the file. 

2. ** Analyse the results

## Project Results

| Model <br> Type | Train <br> Data | Beam <br>Size | Test <br> Data | Test <br> size | Bleu                     |
|-----------------|-----------------|---------------|----------------|----------------|--------------------------|
| LIN             | Split 1         | 5             | split_1_val    | 1,354          | [0.54, 0.39, 0.27, 0.19] |


## Conclusion

Thank you for exploring our project, and we hope our work enriches your understanding of personality traits and clustering techniques.

---

## Data Splits

| Split   | Holdout Pairs                                                        | Train Size | Test Size |
|---------|----------------------------------------------------------------------|------------|-----------|
| Split 1 | black cat, big bird, red bus, small plane, eat man, lie woman        | 79,836     | 1,354     |
| Split 2 | brown dog, small cat, white truck, big plane, ride woman, fly bird   | 79,858     | 1,342     |
| Split 3 | white horse, big cat, blue bus, small table, hold child, stand bird  | 79,940     | 1,455     |
| Split 4 | black bird, small dog, white boat, big truck, eat horse, stand child | 79,627     | 1,503     |
| Control |                                                                      | 79,815     |           |

