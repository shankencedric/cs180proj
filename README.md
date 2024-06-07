# MantisMinds™️ -- CS 180 Final Project
This serves as the final project for CS 180 under Ma'am Lyn, AY 2023-2024, Semester 2. 

[Repo link](https://github.com/shankencedric/cs180proj).


This README file will explain the code structure and how it is run. Importantly, the following: (1) attribution to any data sources used or code bases reused, (2) links to any models that you yourself trained and stored on the cloud (i.e.,Google Drive), and (3) links to datasets you used and/or cleansed versions thereof (again, stored on the cloud).

# Models and Datasets
It is required to have both trained models present in the `models` subfolder of this repository or directory. This is the case by default--although it is possible that these models are not the most up to date.

For reference, they are the following (Google Drive links):
- [`tunedModel.pkl`](https://drive.google.com/file/d/1-7supJLQgEljedoTXssnzaHOlvuvJGso/view?usp=sharing)
- [`tunedModelNH.pkl`](https://drive.google.com/file/d/1-4ILWoj0-gJqZQYUzG1AqwR0M034leTj/view?usp=sharing)

For reference as well, the dataset that was used to train the models is from [Performance vs Predicted Performance](https://www.kaggle.com/datasets/daphnelenders/performance-vs-predicted-performance/), uploaded by Kaggle user CALATHEA21, which directly sampled from
the dataset [Student Alcohol Consumption](https://www.kaggle.com/datasets/uciml/student-alcohol-consumption), uploaded by UCI Machine Learning in colaboration with Dimitry Batogov. 

Note that the former dataset is also optionally included in this reporsitory inside the `dataset-source` folder.

# Prerequisites
To be able to run the demo code `demo.py`, make sure you have Python installed with the recommended version `Python 3.12.3` which is the latest as of June 7, 2024. 

Next, install the prerequisite packages via the following command:
```
pip install joblib scikit-learn==1.5.0 pandas
```

The former (i.e., `joblib`) is used for programmatically importing the models. The middle one (i.e., `scikit-learn` or `sklearn`) is used for understanding and basically making use of the models. The latter (i.e., `pandas`) is used later on to help structure the input into a format readable for model prediction.

# Code Structure
The code has 3 functions: the input function `getInput`, and the predictor functions `predictHuman` and `predictNoHuman`. They are self-explanatory, but it might be of interest to know the structure of the code. 

## `main`
First, at the start of `main`, the models are loaded for future use. Note again that the updated models must be present in the `models` subfolder of this directory.

## `getInput()`
Next, the `getInput` function is called. This function is persistent in asking the user each question, making sure all the required input is valid and converted to the desired values properly--if not, it will ask again and again. Note that the `FinalGrade` column is taken out afterwards as it is the target feature, and is not supposed to be fed into the model.

## `predictHuman(inp)`
Afterwards, it determines if the user input the 2 optional fields to be able to use the model `tunedModel.pkl` (the one with human predictions)--and if so, it calls the `predictHuman` function, passing in the preprocessed input from above. This function runs the input into the model `tunedModel.pkl` and returns the output, which is later printed.

Note here that if the user input their actual score, the code computes and prints how far away the prediction was from the final score.

## `predictNoHuman(inp)`
Finally, without determining anything conditional, it does the same with the `predictNoHuman` function and the `tunedModelNH.pkl`, but now passing in the preprocessed input *minus* the 2 optional fields pertaining to human predictions--i.e., the `PredictedGrade` and `StereotypeActivation` columns. 

Note again here that if the user input their actual score, the code computes and prints how far away the prediction was from the final score.
