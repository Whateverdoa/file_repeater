# import pandas as pd
from pathlib import Path
from icecream import ic

file = r"file_in/"
file_2 = r"file_in/done/202105171_maanden.csv"
file_in_map = r"file_in/"
wdir = Path.cwd()
file_in = wdir / file
file_in2= wdir / file_2
folder_file_in = wdir / file_in




#
# ic(wdir)
# ic(file_in.is_file())
file_out_map = wdir / 'file_out/ begineindlijst.csv'
file_out = wdir / "file_out/"
file_out2 = wdir / "file_out/output_2.csv"
file_tmp = wdir / "file_out/tmp"
file_tmp_2 = wdir / "file_out/tmp2"




#
# print(vert.is_dir())
file_concat = Path(r"C:\Users\mike\PycharmProjects\Projekt_lijstbewerken\source\file_out\concat")

file_tmp_2.mkdir(parents=True, exist_ok=True)
file_tmp.mkdir(parents=True, exist_ok=True)


def cleaner(pad):

    dir_to_empty = sorted(Path(pad).glob('*.csv'))

    for file in dir_to_empty:
        file.unlink()



