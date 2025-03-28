import pandas as pd
from sqlalchemy import create_engine


def reding_exel(file_path):
    # خواندن فایل اکسل
    df = pd.read_excel(file_path)

    list_of_dicts = df.to_dict(orient='records')
    return [list_of_dicts, df]


def making_panda(df, tabel_name):
    # ایجاد اتصال به پایگاه داده SQLite
    engine = create_engine('sqlite:///sayad.db')

    # وارد کردن داده‌ها به پایگاه داده
    df.to_sql(tabel_name, con=engine, if_exists='replace', index=False)

    # چاپ پیغام تایید
    print('tabel_dorost_shodesh')


def remove_empty_rows(df):
    """
    حذف ردیف‌های کاملاً خالی از DataFrame
    :param df: DataFrame ورودی
    :return: DataFrame بدون ردیف‌های خالی
    """
    # حذف ردیف‌هایی که تمامی مقادیر آن‌ها خالی هستند
    df_cleaned = df.dropna(how='all')
    return df_cleaned