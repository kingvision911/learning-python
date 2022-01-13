age = int(input("Enter your age: "))

heart_bit_per_hour = 60 * 75

heart_bit_per_day = int(heart_bit_per_hour) * 24

heart_bit_per_month = int(heart_bit_per_day) * 30

heart_bit_per_year = int(heart_bit_per_month) * 12

life_time_heart_bit = int(heart_bit_per_year) * age

print(f"Your life time heart bit is: {life_time_heart_bit}")

