import pandas as pd
import numpy as np
import streamlit as st
from src.extraction import load_data

st.set_page_config(layout='wide')



def load_data():
    return pd.read_csv('/Users/simaozacarias/Documents/data/02-Python/repos/cursoGit/projeto/data/exported/bikes.xlsx')
    
def read_question13(df):


    unico_dono = df1[df1['owner'] == '1st owner'].shape[0]
    unico_dono

    print(f'A base de dados possui {unico_dono} motos de um único dono')

    df_grouped = df1.groupby('owner').agg(
        qty = pd.NamedAgg('id', 'count')
        ).sort_values('qty').reset_index()

    ax = sns.barplot(
            data=df_grouped,
            x = 'owner',
            y = 'qty'
        )

    ax.bar_label(ax.containers[0])

    ax.set(
            title = 'Quantidade de Motos por tipo de dono',
            xlabel = 'Tipo de Dono',
            ylabel = 'Quantidade de donos'
        );

    return None

def main():

    df_raw = load_data()

    st.dataframe(df_raw)

read_question13()

read_question13()

create_answers_section()




if __name__ == '_main_':
    main()


