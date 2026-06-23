def most_varied_app(app_usage):
    pass

app_usage = {
    "Instagram": [60, 55, 65, 60, 70, 55, 60],
    "YouTube": [100, 120, 110, 100, 115, 105, 120],
    "Snapchat": [30, 35, 25, 30, 40, 35, 30]
}

app_usage_2 = {
    "Twitter": [15, 15, 15, 15, 15, 15, 15],
    "Reddit": [45, 50, 55, 50, 45, 50, 55],
    "Facebook": [80, 85, 80, 85, 80, 85, 80]
}

app_usage_3 = {
    "TikTok": [80, 100, 90, 85, 95, 105, 90],
    "Spotify": [40, 45, 50, 45, 40, 45, 50],
    "WhatsApp": [60, 60, 60, 60, 60, 60, 60]
}

print(most_varied_app(app_usage))
print(most_varied_app(app_usage_2))
print(most_varied_app(app_usage_3))
