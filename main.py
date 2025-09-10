print("Welcome to the Time Converter!")
print("This program converts a large number of seconds into hours, minutes, and remaining seconds.\n")

while True:
    # أخذ إدخال المستخدم
    total_seconds = input("Please enter the total number of seconds: ")

    # تحويل المدخل إلى رقم
    total_seconds = int(total_seconds)

    # العمليات الحسابية
    hours = total_seconds // 3600            # عدد الساعات
    remaining_seconds = total_seconds % 3600 # الباقي بعد الساعات
    minutes = remaining_seconds // 60        # عدد الدقائق
    seconds = remaining_seconds % 60         # عدد الثواني المتبقية

    # طباعة النتيجة
    print(f"Hours = {hours} minutes = {minutes} seconds = {seconds}")

    # سؤال المستخدم إذا بده يكمل أو يوقف
    keep_running = input("Do you want to do another calculation? (yes/no): ")

    if keep_running.lower() != "yes":
        break  # كسر اللوب إذا الجواب مش yes

print("Thank you for using the Time Converter!")
