from sklearn.preprocessing import (
    OneHotEncoder, StandardScaler, LabelEncoder,
)
import pandas as pd


def preenche(df, col):
    segmentos = df.loc[df[col].isnull()]['nm_divisao'].unique()
    dic = {}
    for segmento in segmentos:
        temp = df.loc[df['nm_divisao'] == segmento, col].mode()[0]
        dic.update({segmento: temp})

    for segmento in segmentos:
        temp = dic[segmento]
        df.loc[(df[col].isnull()) & (
            df['nm_divisao'] == segmento), col] = temp
    return df


class Clear():

    def drop_code(df):
        """ 
            Parâmetros
            ----------
                df: DataFrame

            Return
            ------
                DataFrame
        """
        if df['nm_divisao'].isnull().sum() > 0:
            segmentos = df.loc[df['nm_divisao'].isnull()]['de_ramo'].unique()
            dic = {}
            for segmento in segmentos:
                temp = df.loc[df['de_ramo'] == segmento, 'nm_divisao'].mode()[0]
                dic.update({segmento: temp})

            for segmento in segmentos:
                temp = dic[segmento]
                df.loc[(df['nm_divisao'].isnull()) & (
                    df['nm_divisao'] == segmento), 'nm_divisao'] = temp

        for col in df.columns:
            if df[col].isnull().sum() > 0:
                df = preenche(df, col)

        return df

    def transformations(df, df_port, col_num, col_ord, col_bin, col_nom):
        """ 
            Responsável para fazer as transformações de LabelEnconder, Normalização e OneHotEncoder

            Parâmetros
            ----------
                df: DataFrame
                df_port: DataFrame do portfólio
                col_num: coluna numerica
                col_ord: coluna ordinal
                col_bin: coluna binaria
                col_nom: coluna nominal

            Return
            ------
                DataFrame
        """

        # Label enconder
        label = LabelEncoder()

        df_train = pd.DataFrame(data=df['id'])
        port_train = pd.DataFrame(data= df_port['id'])

        df_train[col_num] = df[col_num].copy()
        port_train[col_num] = df_port[col_num].copy()

        cols = col_ord + col_bin

        for col in cols:
            df_train[col] = label.fit_transform(df[col])
            port_train[col] = label.transform(df_port[col])


        # Standard Scaler
        features_scaler = col_ord + col_num
        scaler = StandardScaler()
        scaler.fit(df_train[features_scaler])

        df_train.reset_index(drop=True, inplace=True)
        df_train[features_scaler] = pd.DataFrame(data=scaler.transform(
            df_train[features_scaler]), columns=features_scaler)

        port_train[features_scaler] = pd.DataFrame(data=scaler.transform(
            port_train[features_scaler]), columns=features_scaler)


        # One Hot Encoder
        onehot = OneHotEncoder(sparse= False, handle_unknown= 'ignore')
        onehot.fit(df[col_nom[1:]])

        features_one = onehot.get_feature_names(col_nom[1:])

        onehot_df = pd.DataFrame( onehot.transform(df[col_nom[1:]]), columns= features_one)
        onehot_port_df = pd.DataFrame( onehot.transform(df_port[col_nom[1:]]), columns= features_one)

        df_train.reset_index(drop= True, inplace= True)
        port_train.reset_index(drop= True, inplace= True)

        df_train = pd.concat([df_train, onehot_df.copy()], axis=1)
        port_train = pd.concat([port_train, onehot_port_df.copy()], axis=1)
        
        del(onehot_df, onehot_port_df, scaler, onehot)
        return df_train, port_train

