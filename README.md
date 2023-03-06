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

### Code:
Each file starting with extract_papers is used to extract references information from a source. Each of them create a file in extracted_csv folder containing a line for each reference.

Then fusion_sources is used to combined all the generated csv files together. 

### Extracted_csv:
Folder in which csv from API extraction will be stored

### Processed_csv:
Folder in which csv produced with the processed data of the extraction will be stored (e.g the csv of the combination of sources will be here)

---

## Usage

1.Execute every extract_paper notebook to generate the references csv.

2.Execute fusion_source notebook to obtain the final csv (merged.csv).

To add a new source, you just have to generate a csv file name paper_{name_of_your_source} with the following columns: 
name,DOI,publication_year,dataset_used

---
## Credits
This project was done under the supervision of Veronika Cheplygina (IT University of Copenhagen) and Caroline Petitjean (University of Rouen)
