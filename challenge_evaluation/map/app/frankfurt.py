import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
import streamlit_pandas as sp
import pandas as pd
import numpy as np

def app():

    m = leafmap.Map(center=[0, 0], zoom=2)

    raw_data = gpd.read_file(r"C:\Users\alber\OneDrive\Documents\GitHub\vier_gewinnt\data\streamlit2.gpkg")
    raw_data = raw_data.drop(["Neighborhood","Neighborhood_FID","Land_Value"], axis=1)
    gdf = gpd.GeoDataFrame(raw_data)


    all_widgets = sp.create_widgets(gdf)
    res = sp.filter_df(gdf, all_widgets)



    m.add_gdf(res, layer_name="frankfurt")



    m.to_streamlit(height=700)


