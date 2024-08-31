from exel_reading import reding_exel_making_panda
from taking_backup import making_backup
from sqlalchemy import create_engine
from gui2 import *
import chardet

file_path = r'D:\6.xlsx'
tabel_name = 'my_table'
reding_exel_making_panda(file_path, tabel_name)

# tabel_name = 'sayad.db'
# tabel = connect_to_table(tabel_name)
with open("gui2.py") as file:
    exec(file.read())


output_file_path = r'D:\6.xlsx'
engine = create_engine('sqlite:///sayad.db')
making_backup(output_file_path, engine)