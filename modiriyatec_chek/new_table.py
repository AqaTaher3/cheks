from taking_backup import making_backup
from sqlalchemy import create_engine
import pandas as pd

file_path = r'D:\my_tabel_2.xlsx'
tabel_name = 'my_table_1'

# خواندن داده‌ها از فایل اکسل
df = pd.read_excel(file_path)

# ایجاد اتصال به پایگاه داده SQLite
engine = create_engine('sqlite:///sayad.db')

# وارد کردن داده‌ها به پایگاه داده
df.to_sql(tabel_name, con=engine, if_exists='replace', index=False)

# چاپ پیغام تایید
print('جدول با موفقیت ساخته شد')

# ایجاد نسخه پشتیبان
output_file_path = r'D:\my_tabel_2.xlsx'  # نام فایل خروجی برای نسخه پشتیبان
making_backup(output_file_path, engine)
