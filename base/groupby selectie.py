from collections import Counter
import pandas as pd
import base.paden_naar_files as paden
from icecream import ic


def csv_name_giver():
    def naming_a_csv(name, count, exp=".csv"):
        csv_name = f'{paden.file_tmp_2}/{name}_{count:>{0}{5}}{exp}'
        return csv_name

    return naming_a_csv

csv_dataframe = pd.read_csv('file_out/tmp/output_202102663 vv.csv', ',', usecols=['Naam', 'aantalst', 'Rol'])

# maakt van csv een dataframe met nieuwe kolommen
csv_dataframe["pdf"]= 'leeg.pdf'
csv_dataframe["rol_id"] = csv_dataframe['Rol']
csv_dataframe['omschrijving']= ''



grup_csv_sum = csv_dataframe.groupby(by='Rol').sum()
grup_csv_sum.tail()

# maak een groupby geselecteerd op rolnummer of art nummer iets dat de soort bind
grup = csv_dataframe.groupby('Rol')
grup.count()
grup.describe()
# ic(grup.max())
grup.min()

rol1 = grup.get_group(1)
# met deze functie is het mogelijk om de groep te pakken, om te zetten naar csv of whatever

# ic(rol1.tail())
#
# ic(len(grup))
# ic(grup.size())
# grup.aggregate

kolommen = ['Naam', 'aantalst', 'pdf','rol_id','omschrijving']
# twee = pd.DataFrame([["0","0","stans.pdf",'a'] for x in range(5)], columns = kolommen,)
# ic(twee)

ic(list(csv_dataframe.columns))
kolommen_lijst = list(csv_dataframe.columns)

ic(csv_dataframe.info())
ic(csv_dataframe.shape)
ic(csv_dataframe.describe)




def wikkel(eindgetal, rolnummer):
    begin = df_rol.iat[0, 0]
    # eind = eindgetal
    eind = df_rol.iat[eindgetal-1, 0]


    sluit = pd.DataFrame([["0", "0", "stans.pdf", 'a',f'rol {rolnummer} || {begin} - {eind}||{eindgetal} etiketten']
                          for x in range(1)], columns=kolommen, )

    return sluit

# todo functies in module plaatsen, de forloop in een ander forloop plaatsen voor het maken van meerdere files

csvnaam = csv_name_giver()
dflijst = []
dfbegineind = []

for df_rol in range(len(grup)):
    # dit moet netter kunnen:)
    grup.get_group(df_rol + 1).to_csv(csvnaam("rol", df_rol+1))
    # maakt van elke rol een csv file
    rol_nummer = df_rol+1
    df_rol = grup.get_group(df_rol + 1)
    # maakt een dataframe per rol
    twee = pd.DataFrame([["0", "0", "stans.pdf", 'a', ''] for x in range(2)], columns=kolommen, )
    dflijst.append(twee)
    dflijst.append(wikkel(df_rol.shape[0],rol_nummer))
    dflijst.append(twee)
    dflijst.append(df_rol)
    # def voor wikkels en sluit etiket met sum
    dflijst.append(twee)
    dflijst.append(wikkel(df_rol.shape[0],rol_nummer))
    dflijst.append(twee)

    dfbegineind.append(wikkel(df_rol.shape[0],rol_nummer))


newlijst = pd.concat(dflijst)
# als lijst klaar is maakt een dataframe
newlijst.to_csv('newlijst.csv')

begineindlijst= pd.concat(dfbegineind)
#  maakt een csv file van dataframe


begineindlijst.to_csv(paden.file_out_map)


