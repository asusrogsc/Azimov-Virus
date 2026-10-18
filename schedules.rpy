# ============================================
# TIME OF DAY DURATIONS
# ============================================
# Morning:      6:00 - 11:59 (6 hours)
# Afternoon:   12:00 - 17:59 (6 hours)
# Evening:     18:00 - 19:59 (2 hours)
# Night:       20:00 - 5:59 (10 hours)
# ============================================

# ============================================
# HOME CHARACTERS LOCATION SCHEDULES
# ============================================

default home_character_locations = {
    "dad": {
        "morning": "dad_room",
        "afternoon": "dad_room",
        "evening": "dad_room",
        "night": "dad_room",
        "exceptions": [
            {"start_hour": 5, "end_hour": 6, "location": "shower"},
            {"start_hour": 18, "end_hour": 19, "location": "living_room"}
        ]
    },
    "brother": {
        "morning": "brother_room",
        "afternoon": "brother_room",
        "evening": "brother_room",
        "night": "brother_room",
        "exceptions": []
    }
}




# ============================================
# CHARACTER MEAL TIME SLOTS (30 minutes each)
# ============================================

# Breakfast slots (7:00 - 9:00) - 30 min each = 4 slots
default character_meal_times = {
    "nicks": {"room": "201", "breakfast": (7, 0), "lunch": (12, 0), "dinner": (19, 0)},
    "roman": {"room": "202", "breakfast": (7, 30), "lunch": (12, 30), "dinner": (19, 30)},
    "aftb": {"room": "204", "breakfast": (8, 0), "lunch": (13, 0), "dinner": (20, 0)},
    "jund": {"room": "205", "breakfast": (8, 30), "lunch": (13, 30), "dinner": (20, 30)},
    "shas": {"room": "207", "breakfast": (7, 30), "lunch": (12, 0), "dinner": (19, 30)},
    "aman": {"room": "301", "breakfast": (8, 0), "lunch": (13, 0), "dinner": (19, 0)},
    "abhi": {"room": "306", "breakfast": (7, 0), "lunch": (12, 30), "dinner": (20, 30)},
    "aryn": {"room": "307", "breakfast": (8, 30), "lunch": (12, 0), "dinner": (19, 30)},
    "kernel": {"room": "unknown", "breakfast": (7, 0), "lunch": (13, 30), "dinner": (20, 0)},
    "mayank": {"room": "404", "breakfast": (7, 30), "lunch": (12, 30), "dinner": (19, 30)},
}

# ============================================
# CHARACTER WATER COOLER SCHEDULES (15 minutes each, 2 slots per character)
# Times exclude meal times - randomized and overlapping
# ============================================

default character_water_times = {
    "nicks": [(9, 15), (16, 45)],
    "roman": [(8, 30), (14, 0)],
    "aftb": [(10, 45), (15, 15)],
    "jund": [(9, 30), (17, 30)],
    "shas": [(10, 0), (15, 45)],
    "aman": [(9, 45), (16, 15)],
    "abhi": [(8, 15), (15, 30)],
    "aryn": [(10, 30), (16, 0)],
    "kernel": [(11, 15), (17, 45)],
}

# ============================================
# CHARACTER DOOR-OPEN SCHEDULES (30 minutes each, once a day)
# Times when characters are outside their doors or door is open for interaction
# ============================================

default character_door_open_times = {
    "nicks": (11, 0),
    "roman": (11, 30),
    "aftb": (12, 15),
    "jund": (10, 0),
    "shas": (12, 45),
    "aman": (11, 45),
    "abhi": (13, 0),
    "aryn": (13, 30),
    "kernel": (14, 0),
}