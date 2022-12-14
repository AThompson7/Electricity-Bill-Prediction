# Project 4: Electricity Bill Prediction

## Objectives 

* How do different household variables influence the electricity bill?
* Using machine learning to create a regression model that accurately predicts monthly electricity bill.
* Using the model to create an app that allows users to input variables and receive a predicted energy bill for the month.

## Project structure
```
Electricity-Bill-Prediction
|
|__ .ipynb_checkpoints/                  # contains the electricity-checkpoint.ipynb file
|   |__ electricity-checkpoint.ipynb     # checkpoint notebook
|
|__ Resources/                  # contains raw data
|   |__ complete_dataset.csv    # raw data
|
|__ templates/          # contains raw data
|   |__ index.html      # file for local deployment
|
|__ app.py         # app created for local deployment
|
|__ electricity.ipynb  # analysis notebook that contains the etl process and the machine learning models scripts
|
|__ extra_trees_regression_model.pkl  # pkl file used by the app 
|
|__ random_forest_regression_model.pkl  # pkl file used by the app 
|
|__ Electricity_Bill_Prediction.twbx  # tableau workbook used for the visualizations
|
|__ README.md     # Project description

```
## Usage

Activate environment 
```
# activate environment
conda activate PythonData
```

## Datasets 

|No|Source|Link|
|-|-|-|
|1|Kaggle Open Source Datasets|https://www.kaggle.com/datasets/gireeshs/household-monthly-electricity-bill|


## Project Description: Steps

### ETL process:
Checking for null values and invalid data such as negative values for rooms and people in the home. Converting datatypes to int/float values to be used for machine learning. Renaming columns to be easily understandble and checking for categorical data needing to be dummy encoded.
### Machine Learning process:
Using sklearn's train_test_split to create testing and training subsets. Dependent variable was the electricity bill and independent variables were the remaining columns. After scaling the training data using sklearn's StandardScaler, 5 different regression models were tested. Next, hyperparameter tuning was conducted using RandomizedSearchCV on the RandomForestRegressor and ExtraTreesRegressor. The model with the highest test score was then dumped to a pkl file.
### App process: 
The model is loaded into Flask from the pkl file. The user inputs their household specific info by following a questionnaire. The app then returns a predicted monthly energy bill based on the data entered by the user.
### Conclusion:
After hyperparameter tuning the ExtraTreesRegressor returned an accuracy score of 0.855. After subtracting the real values from the models predictions, the mean absolute error was 58.23 Rupees.



# Contributors
- [@AThompson7](https://github.com/AThompson7)
- [@sodacarlos](https://github.com/sodacarlos)