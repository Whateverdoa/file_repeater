from typing import List

import pandas as pd
from pathlib import Path
import base.paden_naar_files as paden
import base.calculations as function

filecsv = r"file_in/Atelier Munro - shirt 3 def.csv"
print(paden.file_in)

file_out = paden.wdir / r"file_out/test.csv"

# with open(paden.file_in, "r", encoding="utf-8") as readf:
#     readline = readf.readlines()
#
# with open(file_out, "w", encoding="utf-8") as fwrite:
#     fwrite.writelines(readline[0:1])
#     for i in range(2):
#         fwrite.writelines(readline[1:])


folder_file_in_lijst = [rol for rol in paden.file_in.glob("*.csv") if rol.is_file()]
aantal_files= len(folder_file_in_lijst)

print(folder_file_in_lijst)

namen_uit_lijst = function.file_name_maker_met_pad(aantal_files, paden.file_out, "PL 560 sets van shirt ")

count = 0
for file in folder_file_in_lijst:

    function.repeater_van_files(file, namen_uit_lijst[count], 570)
    count += 1



