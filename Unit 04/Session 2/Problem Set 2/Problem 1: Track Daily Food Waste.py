def track_daily_food_waste(waste_records):
  pass

waste_records1 = {
    "2024-08-01": [200, 150, 50],
    "2024-08-02": [300, 400],
    "2024-08-03": [100]
}

result = track_daily_food_waste(waste_records1)
print(result)

waste_records2 = {
    "2024-07-01": [120, 80],
    "2024-07-02": [150, 200, 50],
    "2024-07-03": [300, 100]
}

result = track_daily_food_waste(waste_records2)
print(result)
