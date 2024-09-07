import pandas as pd
from sqlalchemy import create_engine

def move_rows_between_tables(engine, source_table='my_table_1', target_table='my_table_2'):
    # اتصال به پایگاه داده
    conn = engine.connect()

    # خواندن داده‌ها از جدول منبع
    try:
        query = f"SELECT * FROM {source_table}"
        df = pd.read_sql(query, conn)
    except Exception as e:
        print(f"خطا در خواندن جدول {source_table}: {e}")
        conn.close()
        return

    # تبدیل مقادیر ستون Date به نوع تاریخ
    try:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    except Exception as e:
        print(f"خطا در تبدیل تاریخ: {e}")
        conn.close()
        return

    # استخراج ماه و روز از ستون تاریخ
    df['Date_MMDD'] = df['Date'].dt.strftime('%m%d').astype(float)

    # فیلتر کردن داده‌ها بر اساس شرایط
    rows_to_move = df[((df['Date_MMDD'] < 300) & (df['Year'].isna())) |
                      ((df['Year'].notna()) & (df['Date_MMDD'] > 1000))]

    if rows_to_move.empty:
        print("هیچ ردیفی برای انتقال یافت نشد.")
        conn.close()
        return

    # ذخیره ردیف‌های فیلتر شده به جدول مقصد
    try:
        rows_to_move.to_sql(target_table, con=engine, if_exists='replace', index=False)
    except Exception as e:
        print(f"خطا در ذخیره داده‌ها به جدول مقصد {target_table}: {e}")
        conn.close()
        return

    # حذف ردیف‌های منتقل شده از جدول منبع
    remaining_rows = df.drop(rows_to_move.index)
    try:
        remaining_rows.to_sql(source_table, con=engine, if_exists='replace', index=False)
    except Exception as e:
        print(f"خطا در حذف ردیف‌ها از جدول منبع {source_table}: {e}")
        conn.close()
        return

    # بستن اتصال به پایگاه داده
    conn.close()
    print(f"ردیف‌های مطابق با شرایط به جدول {target_table} منتقل شدند و از جدول {source_table} حذف شدند.")
