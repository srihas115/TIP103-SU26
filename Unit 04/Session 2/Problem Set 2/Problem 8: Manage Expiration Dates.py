def check_expiration_order(expiration_dates):
  pass

expiration_dates_1 = [
    ("Milk", "2024-08-05"),
    ("Bread", "2024-08-10"),
    ("Eggs", "2024-08-12"),
    ("Cheese", "2024-08-15")
]

expiration_dates_2 = [
    ("Cheese", "2024-08-15"),
    ("Bread", "2024-08-12"),
    ("Eggs", "2024-08-10"),
    ("Milk", "2024-08-05")
]

print(check_expiration_order(expiration_dates_1))
print(check_expiration_order(expiration_dates_2))
