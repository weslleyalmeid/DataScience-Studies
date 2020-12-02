def return_numeric(dataframe):
    aux = []
    for item in dataframe.columns:
        if dataframe[item].dtypes != 'object':
            aux.append(item)
    return aux