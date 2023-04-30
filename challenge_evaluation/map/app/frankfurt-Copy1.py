import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
import streamlit_pandas as sp
import pandas as pd
import numpy as np

def app():

    m = leafmap.Map(center=[0, 0], zoom=2)

    raw_data = gpd.read_file(r"C:\Users\alber\OneDrive\Documents\GitHub\vier_gewinnt\data\streamlit2.gpkg")
    gdf = gpd.GeoDataFrame(raw_data)


    all_widgets = sp.create_widgets(gdf)
    res = sp.filter_df(gdf, all_widgets)
    
    st.write(res)

    m.add_gdf(res, layer_name="frankfurt")


    #predict_x = pd.DataFrame()
    #predict_x[list(res.columns)] = res
    #predict_x = predict_x.drop(["Neighborhood","geometry","Neighborhood_FID","Land_Value"], axis=1)
    #predict_x = predict_x.astype("float")
    #predict_x = predict_x.min()
    #predict_x = np.asmatrix(predict_x)

    #predict_b = pd.read_csv(r"C:\Users\alber\OneDrive\Documents\GitHub\vier_gewinnt\data\coefs_streamlit2.csv")
    #predict_b = predict_b.astype("float")
    #predict_b = np.asmatrix(predict_b)

    #prediction = predict_x @ predict_b 

    #prediction_string = "The minimum value of a 1m² plot of land with the chosen feautures is {}".format(prediction)
    #print(prediction_string)
    
    


    m.to_streamlit(height=700)


