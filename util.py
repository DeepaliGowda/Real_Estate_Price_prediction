# util will contains all the core routines where the server will just do the routing of request & response
import json
import pickle
import numpy as np
#creating global variables
__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
       loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1   
    x= np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round( __model.predict([x])[0],2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open(r"C:\Users\Deepali\Documents\Real Estate Price prediction\server\artifacts\columns.json",'r') as f:  #opening columns.json file
       __data_columns = json.load(f) ['data_columns']  #converting to dict
       __locations = __data_columns[3:] #in columns.json file the location starts from 3 index

    global __model
    with open(r"C:\Users\Deepali\Documents\Real Estate Price prediction\server\artifacts\real_estate_home_price_model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('Kalhalli',1000,2,2))