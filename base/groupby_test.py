import pandas as pd
import base.paden_naar_files as paden
import base.calculations as function
from icecream import ic


file_in = paden.file_out
ic(file_in)



te_groeperen_df = pd.read_csv(file_in, ",")
rollen =  te_groeperen_df.groupby('Rol')


print(type(te_groeperen_df))

tupled = te_groeperen_df.itertuples(index=True, name='Rol')

rol = 1
lijst = []

for rows in tupled:
    naam = f'rol{rows.Rol}'
    csv = f'rol{rows.Rol}.csv'


    if rows.Rol != rol:
        naam = pd.DataFrame(lijst).to_csv(csv)
        rol += 1
        lijst = []


    elif rows.Rol == 64:
        lijst.append(rows)
        naam = pd.DataFrame(lijst).to_csv(csv)


    else:
        lijst.append(rows)

#################################

verwerkte_file_in = pd.DataFrame(te_groeperen_df)

ic(verwerkte_file_in.head())
ic(verwerkte_file_in.shape)
ic(paden.file_out)
verwerkte_file_in.to_csv(paden.file_out)

# hier verdeel je de
group = verwerkte_file_in.groupby('Rol')
group_sum = verwerkte_file_in.groupby('Rol')['aantalst'].sum()
ic(len(group_sum))
ic(type(group))
#todo use groupby for wikkel
rol_aantallen =[]
for aantal in group_sum:
    rol_aantallen.append(aantal)

rol_aant = pd.DataFrame(rol_aantallen, columns =['aantal']).to_csv(paden.file_out2, index=0)
# for rol, i in enumerate(group):
#     # ic(rol)
#     ic(rol)
#     ic(i)
# for rol in group:
#     ic(rol[0:2])

df = pd.read_csv(file_in,",", index_col='Rol')

print(df.head(10))

artikel_nummers_verzameld=df.groupby('Rol').sum()

artikel_nummers_verzameld.to_csv("arg.csv", encoding='utf-8')

df.aantalst.sum() # aantal totale order

aantal_rollen = len(df)
print(aantal_rollen)

print(df.columns)

indexlijst= df.index

print(indexlijst)

art_lijst = []
count = 1
art_lijst.append(f'{df.index[0]}')  # hard coded eerste regel
for i in range(1, aantal_rollen):

    if df.index[i] != df.index[i - 1]:
        count += 1

        art_lijst.append(f'{df.index[i]}')

print(art_lijst)
aantal_art = len(art_lijst)
print(aantal_art)
len(df.groupby('Rol').sum())

