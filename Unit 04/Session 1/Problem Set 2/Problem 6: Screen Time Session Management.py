def manage_screen_time_sessions(actions):
  pass

actions = ["OPEN Instagram", "OPEN Facebook", "CLOSE Facebook", "CLOSE Instagram"]
actions_2 = ["OPEN Instagram", "CLOSE Instagram", "CLOSE Facebook"]
actions_3 = ["OPEN Instagram", "OPEN Facebook", "CLOSE Instagram", "CLOSE Facebook"]

print(manage_screen_time_sessions(actions))
print(manage_screen_time_sessions(actions_2))
print(manage_screen_time_sessions(actions_3))
