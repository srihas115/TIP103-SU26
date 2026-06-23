def filter_records_by_waste_threshold(waste_records, threshold):
  pass

waste_records1 = [
    ("2024-08-01", 150),
    ("2024-08-02", 200),
    ("2024-08-03", 50),
    ("2024-08-04", 300),
    ("2024-08-05", 100),
    ("2024-08-06", 250)
]
threshold1 = 150

result = filter_records_by_waste_threshold(waste_records1, threshold1)
print(result)

waste_records2 = [
    ("2024-07-01", 90),
    ("2024-07-02", 120),
    ("2024-07-03", 80),
    ("2024-07-04", 130),
    ("2024-07-05", 70)
]
threshold2 = 100

result = filter_records_by_waste_threshold(waste_records2, threshold2)
print(result)
