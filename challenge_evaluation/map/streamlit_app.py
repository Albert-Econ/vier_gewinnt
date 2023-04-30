import streamlit as st
from streamlit_option_menu import option_menu
from apps import frankfurt, prediction  

st.set_page_config(page_title="Streamlit Geospatial", layout="wide")


apps = [
    {"func": frankfurt.app, "title": "Frankfurt", "icon": "bi bi-building"},
    {"func": prediction.app, "title": "Prediction", "icon": "bi bi-cpu"},
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Cities",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break
