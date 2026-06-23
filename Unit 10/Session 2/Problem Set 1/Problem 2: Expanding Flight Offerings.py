def min_flights_to_expand(flights):
    pass

flights = {
    'JFK': ['LAX', 'SFO'],
    'LAX': ['JFK', 'SFO'],
    'SFO': ['JFK', 'LAX'],
    'ORD': ['ATL'],
    'ATL': ['ORD']
}

print(min_flights_to_expand(flights))
