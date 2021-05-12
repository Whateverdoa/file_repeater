""" gebruik een csv of excel file en zet de veelvoud in de eerste kolom
    maakt de nieuwe file voor je"""

import pandas as pd
import base.paden_naar_files as paden
import base.calculations as function
from icecream import ic

file_in = r"file_in/veelvoudtest.csv"
ic(paden.file_in)
ic(function.file_to_generator(paden.file_in).head())


generator = function.file_to_generator(paden.file_in).itertuples(index=True)

nieuwe_df = []
# list comprehension omzetten naar df

for rows in generator:

    for i in range(rows.vv):
        #todo if else logic on rolnummer to build wikkel etc..
        nieuwe_df.append(rows)


verwerkte_file_in = pd.DataFrame(nieuwe_df)

ic(verwerkte_file_in.head())
ic(verwerkte_file_in.shape)
ic(paden.file_out)
verwerkte_file_in.to_csv(paden.file_out)
#
# # hier verdeel je de
# group = verwerkte_file_in.groupby('Rol')
# #todo use groupby for wikkel
#
#
# # for rol, i in enumerate(group):
# #     # ic(rol)
# #     ic(type(rol),i)




