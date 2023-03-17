# Date: 20 March 2023
## Who did you help this week ?
I showed code exemples and help Stinna to create the dynamic filter she needs to query OpenAlex

## What helped you this week ?
* different articles about One Class classification

## What did you achieve ?
* Extract keywords for ACDC based on frequency in abstract (+ TF-IDF with other task)
* Generate histogram of keywords from an abstract
* Implementation of One-Class Random Forest from https://hal.science/hal-00862706/document
* Investigate the reason of histogram fill with 0 for paper that references ACDC
* Search for One class classification technics (Parzen, SVM)

## What did you struggle with ?
* The sparse and very variable representation that results from the histogram of keywords makes the classification difficult

## What would you like to work on next week ?
* Maybe look deeper into the classification

## Where do you need help from Veronika ?
* Discuss about what to do next

## Additional notes:

---

# Date: 13 March 2023
## Who did you help this week ?
N/A

## What helped you this week ?
* https://grand-challenge.org/challenges/ and some survey papers to prepare classification labels

## What did you achieve ?
* Improve code to take in consideration OpenCitation Error 500
* Semi automated extraction with dimensions.ai
* Search for the reason some reference are missing for some sources
* Possible list of labels to classify paper's application
* Coverage comparison visualisation

## What did you struggle with ?
* Instability and execution time when recovering venue of a paper during merging of sources

## What would you like to work on next week ?
* Extraction of paper's task

## Where do you need help from Veronika ?
* Choose classification labels
* Confirm what to do next

## Additional notes:

---

# Date: 06 March 2023
## Who did you help this week ?
Show my code about OpenAlex and explained how it worked to Stinna

## What helped you this week ?
* Ahmet Akkoc git (https://github.com/madprogramer/PublicDatasets) to get ideas for the csv and also the general organisation of a project at the ITU
* Article comparing multiple sources (https://link.springer.com/content/pdf/10.1007/s11192-020-03690-4) Maybe outdated as it's from 2020
## What did you achieve ?
* Make the flowchart of the project (at res/flowchart_database.jpg)
* Create a first list of possible sources to use for extraction
* Extraction with OpenAlex, OpenCitation COCI, OpenCitation POCI
* Fusion of multiple sources
* Improved documentation of the project and code comments

## What did you struggle with ?
* Reference are not totally accurate in the APIs (sometimes some references are missing, sometimes it seems like there are also "false" references)
* OpenCitation API is "unstable" lot of crash leading to Error 500.
* No official API for google scholar
* Get the "Reference type" information from the API I use for the moment
* Not great result for paper with manual ground truth

## What would you like to work on next week ?
* Continue to improve reference extraction
* Maybe search for usage of kaggle datasets using (https://www.kaggle.com/datasets/kaggle/meta-kaggle)
* Maybe try to use https://github.com/scholarly-python-package/scholarly for google scholar 

## Where do you need help from Veronika ?
* Check if current results and way of working are "right" 
* Confirm what to do next
## Additional notes:
