import streamlit as st
import leafmap.foliumap as leafmap


def app():

    m = leafmap.Map(center=[0, 0], zoom=2)

    in_shp = '../data/countries.shp'
    m.add_shp(in_shp, layer_name="Countries")

    m.to_streamlit(height=700)
