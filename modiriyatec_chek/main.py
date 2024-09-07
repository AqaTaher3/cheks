from exel_reading import reding_exel, making_panda
from taking_backup import making_backup
from sqlalchemy import create_engine
from table import *
from functions import *

file_path = r'D:\my_table_1.xlsx'
tabel_name = 'my_table'
output_file_path = r'D:\my_table_1.xlsx'
engine = create_engine('sqlite:///sayad.db')  # آدرس پایگاه داده SQLite

# ------------------------------------------------------
old_data = reding_exel(file_path)[0]
old_df = reding_exel(file_path)[1]

# ------------------  duplicates
dup_sayad = find_duplicate_sayads(old_data)
dup_book = find_duplicate_pbook(old_data)

# some chenges on df and making new table  ----
new_data = 11111111111  # fix me
new_df = 2222222222222  # fix me

# -------------  changing data format
old_df['Date'] = pd.to_datetime(old_df['Date'], errors='coerce')
old_df['Date'] = old_df['Date'].dt.date

pands = making_panda(old_df, tabel_name)

#  ------------------------------------------------------

# شروع برنامه
if __name__ == "__main__":
    # اتصال به پایگاه داده و بارگذاری داده‌ها
    conn, df = create_database_connection()

    # ایجاد پنجره اصلی با Tkinter
    root = tk.Tk()
    root.title("چک صیادی")

    # ایجاد و تنظیم Treeview
    tree = setup_treeview(root, list(df.columns))
    load_data_to_tree(tree, df)

    # تنظیم فیلدهای جستجو
    search_entries = setup_search_entries(root, df, lambda: load_data_to_tree(tree, filter_dataframe(df, search_entries)))

    # اتصال رویداد دوبار کلیک برای ویرایش
    tree.bind("<Double-1>", lambda event: handle_double_click(event, tree, df, conn))

    # اجرای پنجره
    root.mainloop()


# --------------- taking  backup -----------------------------------------
making_backup(output_file_path, engine)
# -----------  move some specific rows to another exel file
# move_rows_between_tables(engine, source_table='my_table_1', target_table='my_table_2') !!!! fix me

