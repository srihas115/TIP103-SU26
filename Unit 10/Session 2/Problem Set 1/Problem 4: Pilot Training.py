def can_complete_flight_training(num_courses, flight_prerequisites):
    pass

flight_prerequisites_1 = [['Advanced Maneuvers', 'Basic Navigation']]
flight_prerequisites_2 = [['Advanced Maneuvers', 'Basic Navigation'], ['Basic Navigation', 'Advanced Maneuvers']]

print(can_complete_flight_training(2, flight_prerequisites_1))
print(can_complete_flight_training(2, flight_prerequisites_2))
