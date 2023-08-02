# linguistic-image-captioning

## TODO
1. Change the parse_coco_composplit to receive the path's as parameters
2. Remove the tokens from the envalutate file
   
## Overview

**This project was executed by the HUJI University NLP lab of prop. Omri Abend.**

**Author: Raz Zeevy**

## Introduction


## Project Structure

The project consists of the following key components:
### Prepare Data



### Prepare Model - Clip
- *Annotations (`data/coco/annotations/train_captions.py`):*
- *Image Data (`data/coco/train2014.py`):*
- *Splits dataset .jsons files (`dataset_splits.dataset_splits_#.json`)*: the
- *the bash script (`extract_compo.sh`)*: the
1. **Activate the enviroment**
   ```bash
   source venv/bin/activate.csh
   ```
2. **Run the parsing script for the datasets (`parse_coco_composplit.py`):**
   ```bash
   venv/bin/python parse_coco_composplit.py --clip_model_type ViT-B/32
   ```
    for each splits the output is ..._train.pkl and ..._train_tokens.pkl and for the control
   
### Train Model - Clip

1. **Main Train Sciprt (`train.py`):** 5 models overall are trained :
   - 4 models for each customized split
   - control model
   - (by default created in /compo/)
2. **Main Train Sciprt (`train.py`):** 


### Evaluate - CompoSplit

1. **Main Analysis Script (`main.py`):** This Python script performs the clustering analysis using the KMeans algorithm on the Big Five personality traits data.


## Project Results


## Conclusion

Thank you for exploring our project, and we hope our work enriches your understanding of personality traits and clustering techniques.
---

## Data Splits

| Split   | Heldout Pairs                                | Train Size | Test Size |
|---------|----------------------------------------------|------------|-----------|
| Split 1 | black cat, big bird, red bus, small plane, eat man, lie woman | 79,836     | 1,354     |
| Split 2 | brown dog, small cat, white truck, big plane, ride woman, fly bird | 79,858     | 1,342     |
| Split 3 | white horse, big cat, blue bus, small table, hold child, stand bird | 79,940     | 1,455     |
| Split 4 | black bird, small dog, white boat, big truck, eat horse, stand child | 79,627     | 1,503     |
| Control |  | 79,815   |      |
