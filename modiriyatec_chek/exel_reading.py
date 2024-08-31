import pandas as pd
from sqlalchemy import create_engine


def reding_exel_making_panda(file_path, tabel_name):
    # خواندن فایل اکسل
    df = pd.read_excel(file_path)

    # ایجاد اتصال به پایگاه داده SQLite
    engine = create_engine('sqlite:///sayad.db')

    # وارد کردن داده‌ها به پایگاه داده
    df.to_sql(tabel_name, con=engine, if_exists='replace', index=False)

    # چاپ پیغام تایید
    print('tabel_dorost_shodesh')
