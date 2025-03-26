import jdatetime
from datetime import datetime

chek = [
    ["6/30", 50], ["7/15", 45], ["9/15", 10]
]

# متغیر برای ذخیره مجموع نهایی
total_sum = 0

# محاسبه برای هر مولفه از chek و جمع کردن نتیجه
for i in chek:
    month = int(i[0].split("/")[0])  # استخراج و تبدیل ماه به عدد صحیح
    day = int(i[0].split("/")[1])    # استخراج و تبدیل روز به عدد صحیح
    amount = i[1]  # مبلغ چک

    result = (month * 30 + day) * amount  # محاسبه

    total_sum += result  # اضافه کردن به مجموع

# دریافت تاریخ و زمان جاری سیستم
current_miladi_date = datetime.now()

# استخراج سال، ماه و روز
year = current_miladi_date.year
month = current_miladi_date.month
day = current_miladi_date.day

# تبدیل به تاریخ شمسی
shamsi_date = jdatetime.datetime.fromgregorian(year=year, month=month, day=day)

# نمایش فقط ماه و روز
miladi_month_day = current_miladi_date.strftime("%m-%d")
shamsi_month_day = shamsi_date.strftime("%m-%d")

dataa = shamsi_month_day.split("-")
rooz = int(dataa[0]) * 30 + int(dataa[1]) * len(chek)

total_summ_mablag = 0
for i in chek:
    amount = i[1]  # مبلغ چک
    total_summ_mablag += amount  # جمع مبلغ چک‌ها

# محاسبه نتیجه نهایی
result_final = (total_sum - rooz) / total_summ_mablag if total_summ_mablag != 0 else 0

# محاسبه تعداد 30 روزها و مقدار باقی‌مانده
count_of_30_days = int(result_final) // 30
remaining_days = result_final % 30

# نمایش نتایج
print("نتیجه نهایی:", result_final)
print("تعداد 30 روزهایی که جا می‌شود:", count_of_30_days)
print("مقدار باقی‌مانده:", remaining_days)
print(f"{count_of_30_days}/{remaining_days}")
