import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd


def app():

    m = leafmap.Map(center=[0, 0], zoom=2)

    frankfurt = gpd.read_file("https://github.com/Albert-Econ/vier_gewinnt/blob/main/Map/1%20Land%20Prices/Land_Prices_Neighborhood_Frankfurt_am_Main.gpkg")
    m.add_gdf(frankfurt, layer_name="Frankfurt")
    
    m.to_streamlit(height=700)
