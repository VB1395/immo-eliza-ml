import pandas as pd
from sklearn.model_selection import train_test_split
from catboost import CatBoostRegressor
import pickle

def cleaning_data():
    '''
    cleaning houses.csv file. combining all binary columns into one. Adding values in 
    other aminities column if value is present. Dropping columns with high number of null 
    values. Also deleting rows with high number of null values. Returning new clean_data file. 
    '''
    df= pd.read_csv('./data/houses.csv')

    other_amenities_col = ['fl_furnished','fl_double_glazing','fl_open_fire','fl_swimming_pool','fl_floodzone']
    df['other_amenities'] = df[other_amenities_col].sum(axis=1)
    #droping columns which containing hig number of null vales
    df.drop(['id','nbr_frontages','cadastral_income','epc','surface_land_sqm','fl_terrace','fl_garden','fl_furnished','fl_double_glazing','fl_open_fire','fl_swimming_pool','fl_floodzone'],axis=1,inplace= True)
    #df =df.dropna(axis=0)
    df = df.dropna(subset=['construction_year','latitude','longitude','primary_energy_consumption_sqm'], axis=0)
    return df.to_csv("./data/clean_data.csv",index=False)

def training():
    '''
    In this function spliting dataset for train and test. test size is 0.2 which is divide
    80% of data for train and 20% for test. Using catboost regression so training input 
    feature columns(object) for encoding. Used hyperparameter tuning for better performance.
    '''
    df= pd.read_csv('./data/clean_data.csv')
    X= df.drop(['price'],axis = 1)
    y= df['price']
    X_train, X_test, y_train, y_test= train_test_split(X,y,test_size= 0.2, random_state= 42)
    # get the column index from a column name
    categorical_feature = [X_train.columns.get_loc(col) for col in X_train.select_dtypes(include=['object']).columns]
    model= CatBoostRegressor(iterations=500, learning_rate=0.1, depth=6, verbose=0)
    model.fit(X,y,cat_features= categorical_feature)

    # Pickle the model
    with open('model.pkl', 'wb') as file: #writing binary file for module
        pickle.dump(model, file)


    print("Pickle file is created")
