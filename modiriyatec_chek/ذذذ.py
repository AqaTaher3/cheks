import jdatetime
from datetime import datetime

chek = [
    ["11/15", 90], ["9/20", 5]
]

# دریافت تاریخ و زمان جاری سیستم
current_miladi_date = datetime.now()
current_shamsi_date = jdatetime.datetime.fromgregorian(year=current_miladi_date.year, month=current_miladi_date.month,
                                                       day=current_miladi_date.day)

# متغیر برای جمع کردن وزن‌ها و فاصله وزنی
total_weighted_distance = 0
total_weights = 0

# محاسبه برای هر مولفه از chek و جمع کردن نتیجه
for i in chek:
    month = int(i[0].split("/")[0])  # استخراج و تبدیل ماه به عدد صحیح
    day = int(i[0].split("/")[1])  # استخراج و تبدیل روز به عدد صحیح
    amount = i[1]  # مبلغ چک

    # تبدیل تاریخ چک به تاریخ شمسی
    check_date = jdatetime.datetime(year=current_shamsi_date.year, month=month, day=day)

    # محاسبه فاصله روزها از تاریخ کنونی
    distance_days = (current_shamsi_date - check_date).days

    # اگر فاصله منفی است، آن را نادیده بگیرید
    if distance_days < 0:
        continue

    # محاسبه فاصله وزنی
    total_weighted_distance += distance_days * amount
    total_weights += amount

# محاسبه میانگین وزنی
weighted_average_distance = total_weighted_distance / total_weights if total_weights != 0 else 0

# تبدیل فاصله روزها به ماه و روز
average_months = weighted_average_distance // 30  # تعداد ماه‌ها
remaining_days = weighted_average_distance % 30  # روزهای باقی‌مانده

# نمایش نتیجه
print(f"فاصله میانگین وزنی: {int(average_months)} ماه و {int(remaining_days)} روز")
