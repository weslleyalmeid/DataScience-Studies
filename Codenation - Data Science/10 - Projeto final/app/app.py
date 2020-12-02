import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from clear import Clear
import nn_model as nn
import os
import base64


def reduce_mem_usage(props):
         
    for col in props.columns:
        if props[col].dtype != object and props[col].dtype != bool:  # Exclude strings and bool
            
            # make variables for Int, max and min
            IsInt = False
            mx = props[col].max()
            mn = props[col].min()
                        
            # Make Integer/unsigned Integer datatypes
            if IsInt:
                if mn >= 0:
                    if mx < 255:
                        props[col] = props[col].astype(np.uint8)
                    elif mx < 65535:
                        props[col] = props[col].astype(np.uint16)
                    elif mx < 4294967295:
                        props[col] = props[col].astype(np.uint32)
                    else:
                        props[col] = props[col].astype(np.uint64)
                else:
                    if mn > np.iinfo(np.int8).min and mx < np.iinfo(np.int8).max:
                        props[col] = props[col].astype(np.int8)
                    elif mn > np.iinfo(np.int16).min and mx < np.iinfo(np.int16).max:
                        props[col] = props[col].astype(np.int16)
                    elif mn > np.iinfo(np.int32).min and mx < np.iinfo(np.int32).max:
                        props[col] = props[col].astype(np.int32)
                    elif mn > np.iinfo(np.int64).min and mx < np.iinfo(np.int64).max:
                        props[col] = props[col].astype(np.int64)    
            
            # Make float datatypes 16 bit
            else:
                props[col] = props[col].astype(np.float16)
    return props

def main():

# todo --------------------------------- Sidebar -------------------------------------------
    
    st.sidebar.image('logo.png', use_column_width=True)

    st.sidebar.markdown(
        """ 
            API desenvolvida com a finalidade de recomendar os leads mais 
            aderentes por similaridade utilizando o portfólio de clientes do usuário.
        """
    )

    opt = st.sidebar.radio('Selecione um opção', options=['Exemplo de recomendação', 'Recomendação para seus dados'])
    st.sidebar.markdown('')

    select = st.sidebar.selectbox('', options=(
        'Informações Adicionais', 'Linkedin', 'GitHub', 'Codenation'))
    if select == 'Linkedin':
        st.sidebar.markdown(
            '##     [----------> Linkedin <-----------](https://www.linkedin.com/in/weslleyalmeida/)')
    if select == 'GitHub':
        st.sidebar.markdown(
            '## [----------> GitHub <-----------](https://github.com/weslleyalmeid)')
    if select == 'Codenation':
        st.sidebar.markdown(
            '## [---------> Codenation <---------](https://codenation.dev/)')

    st.image('acelera.jpg', width=700)
    st.markdown('')


# todo ----------------------------- Exemplo de recomendação ----------------------------------------------

    if opt == 'Exemplo de recomendação':
        cols_nominal = ['id',
                        'sg_uf',
                        'de_ramo',
                        'de_natureza_juridica',
                        'nm_divisao'
                        ]

        cols_ordinal = ['de_nivel_atividade',
                        'de_saude_tributaria',
                        'de_faixa_faturamento_estimado']

        cols_nominal_bin = ['fl_email',
                            'fl_telefone']

        cols_numeric = ['idade_empresa_anos']

        cols = cols_nominal + cols_ordinal + cols_nominal_bin + cols_numeric

        port = pd.read_csv('estaticos_portfolio1.csv', usecols= cols)
        port = reduce_mem_usage(port)

        if st.checkbox('Amostra dos Dados'):
            st.markdown('Amostra de dados aleatórios')
            slider = st.slider('Valores', 1, 10, value=5)
            st.write(port.sample(slider))
            img = False

        if st.checkbox('Informações do Dataset'):
            st.markdown('Info')
            aux = pd.DataFrame({'types': port.dtypes,
                                'percentual_faltante': port.isna().mean()})
            st.write(aux)
            st.markdown('Shape')
            st.write(port.shape)

        if st.checkbox('Describe'):
            st.markdown('Describe')
            st.write(port.describe())

        if st.checkbox('Gerar recomendação'):
            st.text('O benefício de impulsionar sua empresa não é tão rápido, aguarde!')

            df_market = pd.read_csv('market_1.csv')
            df_market = reduce_mem_usage(df_market)


            port = Clear.drop_code(port)

            cols_nominal.remove('nm_divisao')
            cols = cols_nominal + cols_ordinal + cols_nominal_bin + cols_numeric
            port = port[cols]

            df_train, port = Clear.transformations(
                df_market, port, cols_numeric, cols_ordinal, cols_nominal_bin, cols_nominal)

            leads = nn.get_leads(port=port, df= df_train, k=2)
            leads = df_market.merge(leads, how='inner', on= 'id')
            leads.drop_duplicates(subset='id', keep='first', inplace=True)


            aux_1 = f'Quantidade de Leads: {leads.shape[0]}'
            aux_2 = f'Setor mais relevante: {leads["setor"].mode()[0]}'
            aux_3 = f'Estado com maior quantidade de leads: {leads["sg_uf"].mode()[0]}'
            st.write(aux_1)
            st.write(aux_2)
            st.write(aux_3)
            
            st.markdown('**Leads mais aderentes:**')
            st.dataframe(leads)

# todo ----------------------- Recomendação para o usuário final -------------------------
    if opt == 'Recomendação para seus dados':

        file = st.file_uploader('Faça o upload do arquivo', type=['csv', 'xlsx'])

        if file is not None:

            cols_nominal = ['id',
                            'sg_uf',
                            'de_ramo',
                            'de_natureza_juridica',
                            'nm_divisao'
                            ]

            cols_ordinal = ['de_nivel_atividade',
                            'de_saude_tributaria',
                            'de_faixa_faturamento_estimado']

            cols_nominal_bin = ['fl_email',
                                'fl_telefone']

            cols_numeric = ['idade_empresa_anos']

            cols = cols_nominal + cols_ordinal + cols_nominal_bin + cols_numeric
            
            try:
                port = pd.read_csv(file, usecols= cols)
                if 'Unnamed: 0' in list(port.columns):
                    port.drop('Unnamed: 0', axis=1, inplace= True)
            except:
                port = pd.read_excel(file, usecols= cols)
                if 'Unnamed: 0' in list(port.columns):
                    port.drop('Unnamed: 0', axis=1, inplace= True)

            if st.checkbox('Amostra dos Dados'):
                st.markdown('Amostra de dados aleatórios')
                slider = st.slider('Valores', 1, 10, value=5)
                st.write(port.sample(slider))
                img = False

            if st.checkbox('Informações do Dataset'):
                st.markdown('Info')
                aux = pd.DataFrame({'types': port.dtypes,
                                    'percentual_faltante': port.isna().mean()})
                st.write(aux)
                st.markdown('Shape')
                st.write(port.shape)

            if st.checkbox('Describe'):
                st.markdown('Describe')
                st.write(port.describe())

            if st.checkbox('Gerar recomendação'):
                st.text('O benefício de impulsionar sua empresa não é tão rápido, aguarde!')

                df_market = pd.read_csv('market_1.csv')
                port = Clear.drop_code(port)

                cols_nominal.remove('nm_divisao')
                cols = cols_nominal + cols_ordinal + cols_nominal_bin + cols_numeric
                port = port[cols]

                df_train, port = Clear.transformations(
                    df_market, port, cols_numeric, cols_ordinal, cols_nominal_bin, cols_nominal)

                leads = nn.get_leads(port=port, df= df_train, k=2)
                leads = df_market.merge(leads, how='inner', on= 'id')
                leads.drop_duplicates(subset='id', keep='first', inplace=True)

                aux_1 = f'Quantidade de Leads: {leads.shape[0]}'
                aux_2 = f'Setor mais relevante: {leads["setor"].mode()[0]}'
                aux_3 = f'Estado com maior quantidade de leads: {leads["sg_uf"].mode()[0]}'
                st.write(aux_1)
                st.write(aux_2)
                st.write(aux_3)
            
                st.markdown('**Leads mais aderentes:**')
                st.dataframe(leads)

                st.markdown('**Caso deseje fazer o download, clique no link abaixo:**')

                if not leads.empty:

                    csv = leads.to_csv(index=False)
                    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
                    href = f'<a href="data:file/csv;base64,{b64}" download="leads.csv">Download</a>'
                    st.markdown(href, unsafe_allow_html=True)

                else:
                    st.markdown('### Espere o processo de recomendação finalizar')

if __name__ == "__main__":
    main()

