import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import functions

def main():

    st.sidebar.image('./logo.png', use_column_width= True)
    file = st.sidebar.file_uploader('Faça o upload do arquivo', type= ['csv', 'xlsx'])

    st.sidebar.markdown('API desenvolvida com intuito de facilitar a análise e exploração de dados, auxiliando o usuário a observação das caracteríticas dos dados sem necessidade de codicação.')
    st.sidebar.markdown('')

    select =  st.sidebar.selectbox('', options= ('Informações Adicionais', 'Linkedin', 'GitHub', 'Codenation'))
    if select == 'Linkedin':
        st.sidebar.markdown('##     [----------> Linkedin <-----------](https://www.linkedin.com/in/weslleyalmeida/)')
    if select == 'GitHub':
        st.sidebar.markdown('## [----------> GitHub <-----------](https://github.com/weslleyalmeid)')
    if select == 'Codenation':
         st.sidebar.markdown('## [---------> Codenation <---------](https://codenation.dev/)')


    st.markdown('# ANÁLISE E EXPLORAÇÃO DE DADOS')
    st.image('./acelera.jpg', width= 610)
    st.markdown('')

    if file is not None:
        try:
            df = pd.read_csv(file)
        except:
            pd.read_excel(file)
        
 
        if st.checkbox('Amostra dos Dados'):
            st.markdown('Amostra de dados aleatórios')
            slider = st.slider('Valores', 1,10, value=5)
            st.write(df.sample(slider))
            img = False

        if st.checkbox('Informações do Dataset'):
            st.markdown('Info')
            aux = pd.DataFrame({'types': df.dtypes,
                                'percentual_faltante': df.isna().sum() / df.shape[0]})
            st.write(aux)
            st.markdown('Shape')
            st.write(df.shape)


        if st.checkbox('Describe'):
            st.markdown('Describe')
            st.write(df.describe())

        if st.checkbox('Correlação'):
            select = st.selectbox('Selecione o formato:', ('Numérico', 'Gráfico'))
            if select == 'Numérico':
                st.markdown('Correlação')
                st.write(df.corr())
            if select == 'Gráfico':
                mask = np.zeros_like(df.corr())
                mask[np.triu_indices_from(mask)] = True
                sns.heatmap(data= df.corr(), annot= True, fmt='.2f', cmap='GnBu', linewidths=.3, mask= mask)
                plt.xticks(rotation= 45)
                st.pyplot()

        if st.checkbox('Gráficos'):
            graficos = ('Boxplot','Barplot', 'Scatterplot', 'Countplot')
            select = st.selectbox('Selecione o tipo de gráfico:', graficos)
            numeric = functions.return_numeric(df)
            
            if select == 'Boxplot':
                x = st.selectbox('Variável X:', numeric)
                y = st.selectbox('Variável Y:', numeric)
                
                if st.button('Gerar Gráfico'):
                    sns.boxplot(x= x, y= y, data= df)
                    st.pyplot()
            
            if select == 'Barplot':
                x = st.selectbox('Variável X:', numeric)
                y = st.selectbox('Variável Y:', numeric)
                if st.button('Gerar Gráfico'):
                    sns.barplot(x= x, y= y, data= df)
                    st.pyplot()

            if select == 'Scatterplot':
                x = st.selectbox('Variável X:', numeric)
                y = st.selectbox('Variável Y:', numeric)
                if st.button('Gerar Gráfico'):
                    sns.scatterplot(x= x, y= y, data= df)
                    st.pyplot()
            
            if select == 'Countplot':
                x = st.selectbox('Variável X:', numeric)
                if st.button('Gerar Gráfico'):
                    sns.countplot(x= x, data= df)
                    st.pyplot()

if __name__ == "__main__":
    main()


