import pandas as pd


def making_backup(output_file_path, engine):
    # خواندن داده‌ها از جدول به DataFrame
    df = pd.read_sql('SELECT * FROM my_table', con=engine)
    df.to_excel(output_file_path, index=False)
    print(f'Data successfully exported to {output_file_path}')
