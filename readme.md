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

in another file :
with open("gui2.py") as file:
    exec(file.read())