import streamlit as st
import pandas as pd

def app():

    predictions = pd.read_csv(r"C:\Users\alber\OneDrive\Documents\GitHub\vier_gewinnt\data\predictions_errors_lasso_ols.csv")
    predictions = predictions.set_index("Neighborhood")
    predictions = predictions.drop("Unnamed: 0", axis=1)
    st.write(predictions)

    mpe_lass = "Lasso mean prediction error: 679.965"
    mpe_ols = "OLS mean prediction error: 1033.909"
    st.write(mpe_lass)
    st.write(mpe_ols)
