import streamlit as st
from multiapp import MultiApp
from apps import home, oil_gas, renewables  # import your app modules here

from PIL import Image

st.set_page_config(
    page_title="Energy Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)


app = MultiApp()

st.sidebar.markdown("""
# energyDashboard
""")

image = Image.open('images/planet.jpg')
st.sidebar.image(image, width=300)

st.write(
    '<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Oil & Gas", oil_gas.app)
app.add_app("Renewables", renewables.app)

# The main app
app.run()

# App Info
st.sidebar.write("Version: 0.0.1")
st.sidebar.write("Last Update: September, 15th, 2021")

st.sidebar.write("[Email](roderickperezaltamar@gmail.com)")
