import pandas as pd
import sqlite3
import tkinter as tk
from tkinter import ttk


def create_database_connection(db_name='sayad.db'):
    """اتصال به پایگاه داده SQLite و بازگرداندن DataFrame"""
    conn = sqlite3.connect(db_name)
    df = pd.read_sql('SELECT * FROM my_table', conn)
    return conn, df


def setup_treeview(root, columns):
    """ایجاد Treeview و تنظیم ستون‌ها"""
    tree = ttk.Treeview(root, columns=columns, show='headings')
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    tree.pack(expand=True, fill='both')
    return tree


def load_data_to_tree(tree, df):
    """داده‌های DataFrame را به Treeview اضافه می‌کند"""
    tree.delete(*tree.get_children())
    for _, row in df.iterrows():
        tree.insert("", "end", values=list(row))


class PlaceholderEntry(tk.Entry):
    """کلاس برای ایجاد ورودی با placeholder"""
    def __init__(self, master=None, placeholder="", color='grey', *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)
        self._add_placeholder()

    def _clear_placeholder(self, e):
        if self['fg'] == self.placeholder_color:
            self.delete(0, tk.END)
            self['fg'] = self.default_fg_color

    def _add_placeholder(self, e=None):
        if not self.get():
            self['fg'] = self.placeholder_color
            self.insert(0, self.placeholder)


def setup_search_entries(root, df, search_function):
    """ایجاد فیلدهای ورودی برای جستجو و تنظیم آنها"""
    search_entries = {}
    for col in df.columns:
        entry = PlaceholderEntry(root, placeholder=f"{col}")  # اضافه کردن عبارت جستجو در ...
        entry.pack(side=tk.LEFT)
        search_entries[col] = entry
        entry.bind("<KeyRelease>", lambda event, column=col: search_function())  # اتصال به تابع جستجو
    return search_entries


def filter_dataframe(df, search_entries):
    """فیلتر کردن DataFrame بر اساس مقدار ورودی‌ها"""
    filtered_df = df.copy()  # ایجاد یک کپی از DataFrame اصلی
    for col, entry in search_entries.items():
        value = entry.get().strip()  # حذف فضای خالی در ابتدا و انتها
        if value and value != f"{col}":  # چک کردن اینکه ورودی خالی یا placeholder نباشد
            filtered_df = filtered_df[filtered_df[col].astype(str).str.contains(value, case=False, na=False)]
    return filtered_df


def handle_double_click(event, tree, df, conn):
    """رویداد ویرایش سلول در صورت دوبار کلیک"""
    item = tree.selection()[0]
    col_index = int(tree.identify_column(event.x).replace('#', '')) - 1
    row = tree.identify_row(event.y)
    col_name = df.columns[col_index]
    current_value = tree.item(item, 'values')[col_index]

    entry = tk.Entry(root)
    entry.insert(0, current_value)
    entry.place(x=event.x_root - root.winfo_rootx(), y=event.y_root - root.winfo_rooty())

    def save_edit(event):
        new_value = entry.get()
        df.at[int(row[1:], 16) - 1, col_name] = new_value
        load_data_to_tree(tree, df)
        entry.destroy()
        df.to_sql('my_table', conn, if_exists='replace', index=False)

    entry.bind("<Return>", save_edit)



