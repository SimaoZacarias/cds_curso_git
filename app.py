import pandas as pd
import numpy as np
import streamlit as st
from src.extraction import load_data

st.set_page_config(layout='wide')



def load_data():
    return pd.read_csv('/Users/simaozacarias/Documents/data/02-Python/repos/cursoGit/projeto/data/exported/bikes.xlsx')
    
def main():

    df_raw = load_data()

    st.dataframe(df_raw)

if __name__ == '_main_':
    main()
