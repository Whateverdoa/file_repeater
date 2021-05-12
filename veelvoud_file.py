import pandas as pd
import PySimpleGUI as sg
from pathlib import Path
import base.calculations as function
from icecream import ic
from openpyxl import load_workbook
import xlrd
import xlwt


sg.ChangeLookAndFeel('Black')

import sys

if len(sys.argv) == 1:
    fname = sg.popup_get_file('csv of xls file: De kolom met header "veelvoud" is de aantal per regel')
else:
    fname = sys.argv[1]

if not fname:
    sg.popup("Cancel", "No filename supplied")
    raise SystemExit("Cancelling: no filename supplied")
else:
    # sg.popup('The filename you chose was', fname)
    pad = Path(fname)
    print("volledig pad:")
    ic(pad.parent)
    print("naam file met suffix:")
    print(pad.name)
    print("naam file:")
    ic(pad.stem)
    ic(pad.parent)


    generator = function.file_to_generator(pad).itertuples(index=True)
    nieuwe_df = []

    for rows in generator:

        for i in range(rows.veelvoud):
            # todo if else logic on rolnummer to build wikkel etc..
            nieuwe_df.append(rows)

    verwerkte_file_in = pd.DataFrame(nieuwe_df)

    ic(verwerkte_file_in.head())
    ic(verwerkte_file_in.shape)

    paduit = f'{Path(pad.stem)}_verveel_vuldigd_{pad.suffix}'
    ic(paduit)
    ic(pad.suffix)
    ic(pad.joinpath(paduit))

    if pad.suffix == ".csv":

        verwerkte_file_in.to_csv((pad.parent).joinpath(paduit))
    elif  pad.suffix == ".xls" or ".xlsx":
        verwerkte_file_in.to_excel((pad.parent).joinpath(paduit))










    #
    # df = pd.read_csv(fname, ";")
    # print(df.head())
    #
    # print(df.aantal.sum())

    # trespa_base = pd.read_csv(fname, ";")
    #
    # df1 = pd.DataFrame(trespa_base)
    # a = df1['Colorcode']
    # b = df1['num']
    #
    # regex = r"([. -])"
    # subst = ""
    #
    # links = []
    # # try except inbouwen voor als eerste regel een integer bevat!!!!
    # for line in a:
    #     line = str(line)
    #     print(line)
    #     a = "".join(line.strip("\n"))
    #     result = re.sub(regex, subst, a, 0, re.MULTILINE)
    #     links.append(f'{result}-')
    #
    # rechts = [str(line) for line in b]
    #
    # # code = [i + j for i, j in zip(links, rechts)]
    #
    # code_word = pd.DataFrame([i + j for i, j in zip(links, rechts)])
    #
    # print(code_word.head(2))
    #
    # df1['code'] = code_word
    #
    # zonder_csv = fname.split(".csv")
    # a = ''.join(zonder_csv)
    #
    # print(f'zonder csv:{pad.stem}')
    # df1.to_csv(f'{pad.parent / pad.stem}_metcode.csv', ";", index=0)
    #
    # print(df1.head(1))
    # print(df1.tail(1))