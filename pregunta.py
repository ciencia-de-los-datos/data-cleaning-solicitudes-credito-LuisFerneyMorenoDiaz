"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #
    # Inserte su código aquí
    #


    df.dropna(inplace=True)

    df = df.apply(lambda x: x.astype(str)
                  .str.replace("_", "-")
                  .str.replace("-", " ")
                  .str.replace("$", "")
                  .str.replace(",", ""))

    df.loc[:, df.dtypes=='object']=df.loc[:, df.dtypes=='object'].apply(lambda row: row.str.lower())
    df.fecha_de_beneficio = pd.to_datetime(df['fecha_de_beneficio'],format="mixed",dayfirst=True)
    df.monto_del_credito = df.monto_del_credito.astype(float)
    df.drop_duplicates(inplace=True)

    return df
