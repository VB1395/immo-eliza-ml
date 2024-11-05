# 🏡 Real Estate Price Prediction - Immo Eliza

## 🏢 Description

This project uses machine learning models to predict real estate prices in Belgium. The goal is to provide accurate price estimates based on key property features such as location, size, and number of bedrooms.

## 📦 Repo structure
```.
├── data/
│ |── clean_data.csv
| ├── houses.csv
| ├── test_output.csv
| ├── test.csv
├── Notebooks/
│ ├── CatBoost.ipynb
│ ├── clean_data.ipynb
│ ├── RandomForest.ipynb
├── .gitignore
├── model.pkl
├── predict.py
├── README.md
├── requirements.txt
└── train.py
```
## Model training

I have iteratively tested various algorithms to train and evaluate multiple ML models.

Here is an example of the evaluation results for the test set, with three different algorithms:

```

| Model           | MAE         |   RMSE         | R2    |
|                 |             |                |       |
| LinearRegressor | 157,736.80  | 349,050.53     | 0.42  |
| Random Forest   |  93,743.94  | 199,429.04     | 0.81  |
| CatBoost        |  92,223.55  | 199,075.41     | 0.81  |

```
## 👩‍💻 Usage

1. Clone the repository to your local machine.

2 .Set Up Your Environment:

Ensure you have the necessary libraries installed. You can do this by running:

```bash
  pip install -r requirements.txt
  
```

### Training a Model & Making Predictions

1. Update the `train.py` and `predict.py` script with your correct path of the file. 
2. Run `predict.py` to preprocess the new dataset and make predictions. Your predictions are saved to a .csv in the `test_output.csv/` file

```

python predict.py

```

## ⚠️ Limitations

- The model relies heavily on the quality and comprehensiveness of the input data.
- It does not account for market trends or economic conditions.
- The model's predictions are specific to Belgium and may not generalize well to other regions.



## ⏱️ Timeline

This project took 5 days for completion.

## 📌 Contributors
This project was done as part of the AI Boocamp at BeCode.org. 

Find me on [LinkedIn](https://www.linkedin.com/in/veena-bhawani-b41804111/) for collaboration, feedback, or to connect.