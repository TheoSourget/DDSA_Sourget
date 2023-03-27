# DDSA Sourget Théo

## Objective of the project
This project aims to study the usage of datasets in research papers related to medical image segmentation. The code allows you to get informations of which dataset is used by a paper and what type of task a paper is solving (e.g heart segmentation, brain segmentation, etc...).

---

## Structure of the project

### Data:
Refer to data/keys.csv for the complete description of each field of the different csv file.
1. datasets.csv is the list of dataset with the relative task of the dataset.
2. papers_gt.csv is the list of papers with manual annotation to check the results of automatic extraction.
3. paper.csv is the list of paper we want to extract values from.
4. dataset_labels.csv is the list of possible keyword/label for a dataset
5. dimension folder contains a csv for each dataset. Every file contains the list of citations exported from dimensions.ai
6. keywords.csv is the list of word we search in paper abstract to create the groundtruth for paper classification

### Code:

* references_extraction folder: Aim to extract the references of papers

    - Each file starting with extract_papers is used to extract references information from a source. Each of them create a file in extracted_csv folder containing a line for each reference.

    - Then fusion_sources is used to combined all the generated csv files together. 


* task_classification folder: Aim to extract the task of a paper
    - create_dataset: Create dataset of abstract and task according to simple keywords (e.g cardiac, brain, acdc, etc...)
    - taskExtraction/abstract_classification/bluebert_classif is used to extract the task of a paper using its abstract by searching for keywords computed by looking at the most present words in paper referencing a specific dataset (e.g ACDC for cardiac segmentation task) and creating the histogram of these keywords in an abstract to then apply one class classification technics
    - OCRF is the implementation of One-Class Random Forest as described in https://hal.science/hal-00862706/document

* other folder: Everything that doesn't fit in other folders (mostly analysis script)

    * CoverageAnalysis is used to analyse the return papers of a sources and compare them

### Results:
This folder will contain the output of the different scripts
* extracted_csv will store raw csv produced by references extraction script

* processed_csv will store csv produced with the processed data of the reference extraction (e.g the csv of the combination of sources will be here)

* classification will store output of script used to classify the task of a paper
Folder in which csv from API extraction will be stored

* other will store output that doesn't fit into other categories

### Ressources:
Papers, generated figures or scheme

---

## Installation
1. clone the project 
```console
git clone https://github.com/TheoSourget/DDSA_Sourget.git
```
2. install requirements
```console
cd DDSA_Sourget
pip3 install -r requirements.txt
```

---

## Usage

### Make the extraction

1. Execute every extract_paper notebook to generate the references csv.
2. Execute fusion_source notebook to obtain the final csv (merged.csv).


### Make the classification
1. Update the dataset if wanted using code/task_classification/create_dataset.ipynb
2. Train and test classifiers in code/task_classification/abstract_classification.ipynb

### Add new elements
1. References extraction

    To add a new source to merge with other, you just have to generate a csv file name paper_{name_of_your_source} with the following columns: 
    name,DOI,publication_year,dataset_used

    To add a new dataset in existing extraction with OpenAlex and OpenCitation, put in datasets.csv a new line with the dataset information

    To add a new dataset with dimensions.ai, fusion all the exported files into a single file that respect the format of dimensions.ai (first line of the csv for query information and second line as csv header). The file should be named {name_of_dataset}.csv

2. Create the dataset
    To add a new keyword to check in the abstracts, just add in data/keywords.csv a new line with (keyword,organ) and then launch the related cells in code/task_classification/create_dataset.ipynb

---
## Credits
This project was done under the supervision of Veronika Cheplygina (IT University of Copenhagen) and Caroline Petitjean (University of Rouen)

To make this project we've used the following tools:

* <b>OpenAlex</b>: Priem, J., Piwowar, H., & Orr, R. (2022). OpenAlex: A fully-open index of scholarly works, authors, venues, institutions, and concepts. ArXiv. https://arxiv.org/abs/2205.01833
* <b>OpenCitation</b>: https://opencitations.net/
* <b>Dimensions.ai</b>: Digital Science. (2018-) Dimensions [Software] available from https://app.dimensions.ai. Accessed on 2023, under licence agreement. 