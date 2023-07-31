# linguistic-image-captioning

## TODO
1. Change the parse_coco_composplit to receive the path's as parameters
2. Add random sampling from the dataset for control model to be the same size as test 
   
## Overview

**This project was executed by the HUJI University NLP lab of prop. Omri Abend.**

**Author: Raz Zeevy**

## Introduction


## Project Structure

The project consists of the following key components:

### Prepare
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
    for each splits the output is ..._train.pkl and ..._train_tokens.pkl
   
### Train

1. **Main Train Sciprt (`train.py`):** 5 models overall are trained :
   - 4 models for each customized split
   - control model
   - (by default created in /compo/)
2. **Main Train Sciprt (`train.py`):** 


### Evaluate

1. **Main Analysis Script (`main.py`):** This Python script performs the clustering analysis using the KMeans algorithm on the Big Five personality traits data.

2. **Personality Traits Data (`data-final.csv`):** The dataset contains responses to personality assessment questions that quantify the Big Five traits for a group of individuals.

3. **Notebook (`Neuro.ipynb`):** An optional Jupyter Notebook that contains additional analyses or experimentation.

4. **Plots (`plots` directory):** This directory contains generated heatmaps and statistics plots for different cluster configurations.

## Project Results



## Conclusion



Thank you for exploring our project, and we hope our work enriches your understanding of personality traits and clustering techniques.

---

