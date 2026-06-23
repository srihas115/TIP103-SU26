def manage_food_waste_with_queue(waste_records):
  pass

waste_records_1 = [
    ("2024-08-01", 150),
    ("2024-08-02", 120),
    ("2024-08-03", 100),
    ("2024-08-04", 80),
    ("2024-08-05", 60)
]

waste_records_2 = [
    ("2024-08-01", 150),
    ("2024-08-02", 180),
    ("2024-08-03", 160),
    ("2024-08-04", 140),
    ("2024-08-05", 120)
]

print(manage_food_waste_with_queue(waste_records_1))
print(manage_food_waste_with_queue(waste_records_2))
