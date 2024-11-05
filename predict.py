import pickle
import pandas as pd
from train import cleaning_data, training

def predict():
    '''
    In this function using model which was trained before for predicting prices. It will 
    take test file as input and return test_ouput.csv with predicted price columns for 
    houses. 
    '''
    with open('model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)

    #prediction= loaded_model.predict([['APARTMENT','APARTMENT','Flanders','Antwerp','Antwerp',
    #2050, 51.2171725, 4.3799821, 1963, 100, 2, 'INSTALLED',	5,0,'MISSING',231,'GAS'	, 1]])
    df = pd.read_csv('./data/test.csv')
    predictions=loaded_model.predict(df)
    pred_to_column= pd.DataFrame(data= predictions, columns=['Price'])
    final_file= pd.concat([pd.read_csv('./data/test.csv'),pred_to_column],axis =1)
    final_file.to_csv('./data/test_ouput.csv', header=True, index=False)
    print("Price column added to csv")


if __name__ == "__main__":
    cleaning_data()     # cleaning data
    training()          # training data    
    predict()           # predicting prices for houses

