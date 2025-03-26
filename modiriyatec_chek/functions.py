from datetime import datetime


def find_duplicate_sayads(data):
    sayad_count = {}
    duplicates = set()  # استفاده از set برای جلوگیری از تکرار مقادیر در لیست نهایی

    # شمارش تعداد تکرار هر Sayad
    for item in data:
        sayad = item.get('Sayad')

        # نادیده گرفتن مقادیر gadimi و نرمال‌سازی داده‌ها
        if sayad and sayad != '**gadimi**':
            sayad = str(sayad).strip()  # تبدیل به رشته و حذف فضاهای اضافی

            if sayad in sayad_count:
                sayad_count[sayad] += 1
                duplicates.add(sayad)  # اضافه کردن به set مقادیر تکراری
            else:
                sayad_count[sayad] = 1

    print(duplicates)  # تبدیل set به لیست برای خروجی


def find_duplicate_pbook(data):
    book_count = {}
    duplicates = set()  # استفاده از set برای جلوگیری از تکرار مقادیر در لیست نهایی

    # شمارش تعداد تکرار هر Sayad
    for item in data:
        book = item.get('BooK')

        # نادیده گرفتن مقادیر gadimi و نرمال‌سازی داده‌ها
        if book and book != '**gadimi**':
            book = str(book).strip()  # تبدیل به رشته و حذف فضاهای اضافی

            if book in book_count:
                book_count[book] += 1
                duplicates.add(book)  # اضافه کردن به set مقادیر تکراری
            else:
                book_count[book] = 1

    print(duplicates)  # تبدیل set به لیست برای خروجی


# not using for now
def convert_date_format(data):
    for item in data:
        if 'Date' in item and item['Date']:
            try:
                # تبدیل مقدار 'Date' به datetime object
                date_obj = datetime.strptime(item['Date'], '%Y-%m-%d %H:%M:%S.%f')

                # استخراج ماه و روز به فرمت MMDD
                new_format = f"{date_obj.month:02}{date_obj.day:02}"  # تبدیل ماه و روز به فرمت 'MMDD'

                # جایگزینی فرمت جدید در داده
                item['Date'] = new_format
            except ValueError:
                # اگر فرمت تاریخ نادرست بود، از آن صرف‌نظر کنید
                continue
            except TypeError:
                continue
    return data
