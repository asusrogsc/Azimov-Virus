

# ============================================
# HOSTEL EXPLORATION SYSTEM
# ============================================

init python:
    # Game time tracking (in 24-hour format)
    class GameTime:
        def __init__(self, hour=7, minute=0, day=1, month=1, year=2024):
            self.hour = hour
            self.minute = minute
            self.day = day
            self.month = month
            self.year = year
        
        def advance_time(self, hours=0, minutes=30):
            self.minute += minutes
            self.hour += hours
            
            if self.minute >= 60:
                self.hour += self.minute // 60
                self.minute = self.minute % 60
            
            if self.hour >= 24:
                days_to_add = self.hour // 24
                self.hour = self.hour % 24
                self.advance_days(days_to_add)
        
        def advance_days(self, days=1):
            """Advance the date by specified number of days"""
            import datetime
            current_date = datetime.date(self.year, self.month, self.day)
            new_date = current_date + datetime.timedelta(days=days)
            self.year = new_date.year
            self.month = new_date.month
            self.day = new_date.day
        
        def get_time_string(self):
            return "{:02d}:{:02d}".format(self.hour, self.minute)
        
        def get_date_string(self):
            """Return date as format: '1st January, Saturday'"""
            import datetime
            date_obj = datetime.date(self.year, self.month, self.day)
            
            # Month names
            months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            
            # Day names
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            
            # Get day of week (0 = Monday, 6 = Sunday)
            day_of_week = date_obj.weekday()
            day_name = days[day_of_week]
            
            # Get ordinal suffix (1st, 2nd, 3rd, 4th, etc.)
            day = self.day
            if day in [1, 21, 31]:
                suffix = "st"
            elif day in [2, 22]:
                suffix = "nd"
            elif day in [3, 23]:
                suffix = "rd"
            else:
                suffix = "th"
            
            month_name = months[self.month - 1]
            return "{}{}".format(day, suffix) + " " + month_name + ", " + day_name
        
        def is_breakfast_time(self):
            return 7 <= self.hour < 9
        
        def is_lunch_time(self):
            return 12 <= self.hour < 14
        
        def is_dinner_time(self):
            return 19 <= self.hour < 21
        
        def get_meal_available(self):
            if self.is_breakfast_time():
                return "breakfast"
            elif self.is_lunch_time():
                return "lunch"
            elif self.is_dinner_time():
                return "dinner"
            return None

default game_time = GameTime(hour=7, minute=0, day=12, month=1, year=2026)
default current_location = "room"
default previous_location = "room"
default inventory = []  # Inventory for items/food
default met_characters = []  # Track which characters you've met
default water_bottle_full = True  # Track if Madd's water bottle is full

# ============================================
# CHARACTER RELATIONSHIP SYSTEM
# ============================================
# Each character has relationship values:
# - Friend: Increases when introduced, talked to, or positive interactions
# - Lust: Increases when they see Madd in hot/embarrassing situations
# - Identity: Increases when they discover Madd is female
# - Dominance: How dominant/superior the character acts (affects dialogue tone)
# - Anger: Current anger level (affects mood and harshness)

default hostel_character_relations = {
    "nicks": {"friend": 0, "lust": 0, "identity": 0, "dominance": 75, "anger": 0},
    "roman": {"friend": 0, "lust": 0, "identity": 0, "dominance": 75, "anger": 0},
    "aftb": {"friend": 0, "lust": 0, "identity": 0, "dominance": 78, "anger": 0},
    "jund": {"friend": 0, "lust": 0, "identity": 0, "dominance": 50, "anger": 0},
    "shas": {"friend": 0, "lust": 0, "identity": 0, "dominance": 77, "anger": 0},
    "aman": {"friend": 0, "lust": 0, "identity": 0, "dominance": 50, "anger": 0},
    "abhi": {"friend": 0, "lust": 0, "identity": 0, "dominance": 50, "anger": 0},
    "aryn": {"friend": 0, "lust": 0, "identity": 0, "dominance": 50, "anger": 0},
    "kernel": {"friend": 0, "lust": 0, "identity": 0, "dominance": 72, "anger": 0},
    "mayank": {"friend": 0, "lust": 0, "identity": 0, "dominance": 80, "anger": 0},
}

# Madd's attributes
default madd_dominance = 50
default madd_anger = 0
default mayank_visited_today = False
default last_mayank_visit_hour = -1
default water_fills_today = 0
default last_water_fill_hour = -1
default interceptions_today = 0
default last_interception_hour = -1



# ============================================
# TIME-BASED IMAGE HELPER FUNCTION
# ============================================

init python:
    def get_time_of_day(game_time):
        """
        Determine the time of day based on hour.
        Returns 'morning', 'evening', or 'night'
        """
        hour = game_time.hour
        if 6 <= hour < 18:
            return "morning"
        elif 18 <= hour < 21:
            return "evening"
        else:
            return "night"
    
    def get_location_image(location, game_time, character_meal_times=None):
        """
        Get the appropriate background image based on location and time of day.
        For 1st floor (dining), shows crowded version if characters are eating.
        """
        time_of_day = get_time_of_day(game_time)
        
        # Room 305 (Madd's room) - uses scene 305 images
        if location == "room":
            return f"scene 305 {time_of_day}"
        
        # 2nd Floor - uses 2f images
        elif location == "floor_2":
            return f"scene 2f {time_of_day}"
        
        # Corridors on floors 3, 4 - use corridor images
        elif location in ["hallway_3rd", "floor_4"]:
            return f"scene corridor {time_of_day}"
        
        # 1st Floor - check if anyone is eating
        elif location == "floor_1":
            if character_meal_times:
                # Check if any character is currently eating (within their 30-min slot)
                meal_type = get_meal_type(game_time)
                if meal_type and is_anyone_eating(game_time, character_meal_times, meal_type):
                    # Use crowded version if available
                    if time_of_day == "morning":
                        return "scene 1f morning crowded"
                    elif time_of_day == "night":
                        return "scene 1f night crowded"
            # Default to regular image
            return f"scene 1f {time_of_day}"
        
        # Default fallback
        else:
            return "bg room"
    
    def get_meal_type(game_time):
        """
        Determine which meal time it is.
        Returns 'breakfast', 'lunch', 'dinner', or None
        """
        hour = game_time.hour
        minute = game_time.minute
        
        if 7 <= hour < 9:
            return "breakfast"
        elif 12 <= hour < 14:
            return "lunch"
        elif 19 <= hour < 21:
            return "dinner"
        return None
    
    def is_anyone_eating(game_time, character_meal_times, meal_type):
        """
        Check if any character is currently eating during their meal slot.
        Each character has a 30-minute slot starting at their meal time.
        """
        current_hour = game_time.hour
        current_minute = game_time.minute
        
        for character, meal_times in character_meal_times.items():
            if meal_type in meal_times:
                slot_hour, slot_minute = meal_times[meal_type]
                slot_end_hour = slot_hour
                slot_end_minute = slot_minute + 30
                
                if slot_end_minute >= 60:
                    slot_end_hour += 1
                    slot_end_minute -= 60
                
                # Check if current time is within this character's meal slot
                current_time_minutes = current_hour * 60 + current_minute
                slot_start_minutes = slot_hour * 60 + slot_minute
                slot_end_minutes = slot_end_hour * 60 + slot_end_minute
                
                if slot_start_minutes <= current_time_minutes < slot_end_minutes:
                    return True
        
        return False
    
    def is_mayank_in_reception(game_time):
        """
        Check if Mayank is in reception based on his schedule.
        Reception: 9:00-12:00 and 13:00-16:00
        Room: After 16:00 and before 9:00
        """
        hour = game_time.hour
        minute = game_time.minute
        current_time = hour * 60 + minute
        
        # 9:00 - 12:00
        if 9 * 60 <= current_time < 12 * 60:
            return True
        # 13:00 - 16:00
        elif 13 * 60 <= current_time < 16 * 60:
            return True
        else:
            return False
    
    def get_character_at_water_cooler(game_time, character_water_times):
        """
        Get list of characters currently at the water cooler.
        Each character has 15-minute slots at water cooler.
        Multiple characters can be there at the same time.
        """
        current_hour = game_time.hour
        current_minute = game_time.minute
        current_time_minutes = current_hour * 60 + current_minute
        
        characters_at_cooler = []
        for character, water_slots in character_water_times.items():
            for slot_hour, slot_minute in water_slots:
                slot_start_minutes = slot_hour * 60 + slot_minute
                slot_end_minutes = slot_start_minutes + 15
                
                if slot_start_minutes <= current_time_minutes < slot_end_minutes:
                    characters_at_cooler.append(character)
        
        return characters_at_cooler
    
    def get_character_outside_door(game_time, character_door_open_times):
        """
        Get the character currently outside their door/door is open.
        Each character has a 30-minute slot once a day.
        """
        current_hour = game_time.hour
        current_minute = game_time.minute
        current_time_minutes = current_hour * 60 + current_minute
        
        for character, (door_hour, door_minute) in character_door_open_times.items():
            slot_start_minutes = door_hour * 60 + door_minute
            slot_end_minutes = slot_start_minutes + 30
            
            if slot_start_minutes <= current_time_minutes < slot_end_minutes:
                return character
        
        return None
    
    def get_all_characters_outside_door(game_time, character_door_open_times):
        """
        Get all characters currently outside their door/door is open.
        Returns a list of all characters with open doors at current time.
        """
        current_hour = game_time.hour
        current_minute = game_time.minute
        current_time_minutes = current_hour * 60 + current_minute
        
        characters_outside = []
        for character, (door_hour, door_minute) in character_door_open_times.items():
            slot_start_minutes = door_hour * 60 + door_minute
            slot_end_minutes = slot_start_minutes + 30
            
            if slot_start_minutes <= current_time_minutes < slot_end_minutes:
                characters_outside.append(character)
        
        return characters_outside
    
    def get_characters_at_messhall(game_time, character_meal_times, meal_type):
        """
        Get list of characters currently eating at mess hall for a specific meal.
        Each character has a 30-minute meal slot.
        Multiple characters can be eating at the same time.
        """
        current_hour = game_time.hour
        current_minute = game_time.minute
        current_time_minutes = current_hour * 60 + current_minute
        
        characters_eating = []
        for character, meal_times in character_meal_times.items():
            if meal_type in meal_times:
                slot_hour, slot_minute = meal_times[meal_type]
                slot_start_minutes = slot_hour * 60 + slot_minute
                slot_end_minutes = slot_start_minutes + 30
                
                if slot_start_minutes <= current_time_minutes < slot_end_minutes:
                    characters_eating.append(character)
        
        return characters_eating
    
    def can_madd_ignore(character, madd_dominance, character_relations):
        """
        Check if Madd can ignore a character based on dominance difference.
        If difference > 25, Madd cannot ignore and must interact.
        Returns True if Madd can ignore, False if forced to interact.
        """
        character_dominance = character_relations[character]["dominance"]
        dominance_diff = character_dominance - madd_dominance
        
        # If character's dominance is more than 25 higher than Madd's, Madd must interact
        if dominance_diff > 25:
            return False
        return True
    
    def should_mayank_visit(game_time):
        """
        Check if Mayank should visit Madd in the mess hall.
        Only visits during non-meal hours when he's in reception.
        Has a 40% chance to visit, but only once per in-game day.
        """
        # Check if already visited today
        global mayank_visited_today, last_mayank_visit_hour
        if mayank_visited_today:
            # Reset if it's a new day (hour decreased or went past midnight)
            if game_time.hour < last_mayank_visit_hour and last_mayank_visit_hour != -1:
                mayank_visited_today = False
            else:
                return False
        
        # Check if Mayank is in reception
        hour = game_time.hour
        minute = game_time.minute
        current_time = hour * 60 + minute
        
        in_reception = False
        if (9 * 60 <= current_time < 12 * 60) or (13 * 60 <= current_time < 16 * 60):
            in_reception = True
        
        # Check if it's a non-meal time
        if (7 <= hour < 9) or (9 <= hour < 12) or (12 <= hour < 14) or (14 <= hour < 19) or (19 <= hour < 21):
            is_meal_time = True
        else:
            is_meal_time = False
        
        # Mayank visits during non-meal hours when in reception, with 40% chance
        if in_reception and not is_meal_time:
            return renpy.random.random() < 0.4
        return False
    
    # Floor assignments for characters
    character_floors = {
        "nicks": 2,
        "roman": 2,
        "aftb": 2,
        "jund": 2,
        "shas": 2,
        "aman": 3,
        "abhi": 3,
        "aryn": 3,
        "kernel": 4,
        "mayank": 4,
    }
    
    # Character descriptions for unmet characters
    character_descriptions = {
        "abhi": "OH god he's the definition of chopped, I feel so bad for him",
        "aftb": "Oh god he's so tall and muscular, he must be eating a lot of protein",
        "aman": "This guy looks like he drives a mclaren. If he's so rich why is he here",
        "aryn": "Looks like a skinny dude seems friendly",
        "jund": "He looks like a follower of that religion that does violence to women",
        "mayank": "He's the boss I have met him already, gotta listen to him at all times",
        "roman": "He looks so similar to mayank, the resemblence is uncanny",
        "shas": "He's also very tall wears glasses, looks decently smart",
        "nicks": "He looks pretty smart and confident",
        "kernel": "He looks like he spends a lot of time studying"
    }
    
    def get_characters_observation(current_location, game_time, character_meal_times, character_water_times, character_door_open_times, met_characters):
        """
        Generate a description of characters Madd sees in the current location.
        Includes both met characters (by name) and unmet characters (with descriptions).
        """
        current_time_minutes = game_time.hour * 60 + game_time.minute
        met_characters_seen = {}  # {character_name: location_description}
        unmet_characters_seen = {}  # {character_name: location_description}
        
        if current_location == "floor_1":
            # Check who is eating in mess hall
            if 7 <= game_time.hour < 9:
                meal_type = "breakfast"
            elif 12 <= game_time.hour < 14:
                meal_type = "lunch"
            elif 19 <= game_time.hour < 21:
                meal_type = "dinner"
            else:
                meal_type = None
            
            if meal_type:
                for character, meal_times in character_meal_times.items():
                    if meal_type in meal_times:
                        slot_hour, slot_minute = meal_times[meal_type]
                        slot_start_minutes = slot_hour * 60 + slot_minute
                        slot_end_minutes = slot_start_minutes + 30
                        if slot_start_minutes <= current_time_minutes < slot_end_minutes:
                            if character in met_characters:
                                met_characters_seen[character] = "in the mess hall"
                            else:
                                unmet_characters_seen[character] = "in the mess hall"
        
        elif current_location in ["floor_2", "hallway_3rd", "floor_4"]:
            # Determine which floor the player is currently on
            if current_location == "floor_2":
                player_floor = 2
            elif current_location == "hallway_3rd":
                player_floor = 3
            else:  # floor_4
                player_floor = 4
            
            # Check water cooler (floor 2 only)
            if current_location == "floor_2":
                for character, water_slots in character_water_times.items():
                    for slot_hour, slot_minute in water_slots:
                        slot_start_minutes = slot_hour * 60 + slot_minute
                        slot_end_minutes = slot_start_minutes + 15
                        if slot_start_minutes <= current_time_minutes < slot_end_minutes:
                            if character in met_characters:
                                met_characters_seen[character] = "at the water cooler"
                            else:
                                unmet_characters_seen[character] = "at the water cooler"
            
            # Check door open times (only for characters on the same floor)
            for character, (door_hour, door_minute) in character_door_open_times.items():
                # Only show characters that are on the same floor as player
                if character in character_floors and character_floors[character] == player_floor:
                    slot_start_minutes = door_hour * 60 + door_minute
                    slot_end_minutes = slot_start_minutes + 30
                    if slot_start_minutes <= current_time_minutes < slot_end_minutes:
                        if character in met_characters:
                            met_characters_seen[character] = "in the corridor"
                        else:
                            unmet_characters_seen[character] = "in the corridor"
        
        # Format the observation with both met and unmet characters
        obs_parts = []
        
        # Add met characters
        for char, location in sorted(met_characters_seen.items()):
            obs_parts.append("{} {}".format(char.capitalize(), location))
        
        # Add unmet characters with descriptions
        for char, location in sorted(unmet_characters_seen.items()):
            if char in character_descriptions:
                obs_parts.append("{} {}".format(character_descriptions[char], location))
            else:
                obs_parts.append("some guy I haven't met {}".format(location))
        
        # Format the final observation
        if obs_parts:
            if len(obs_parts) == 1:
                return "I see {}.".format(obs_parts[0])
            else:
                return "I see {} and {}.".format(", ".join(obs_parts[:-1]), obs_parts[-1])
        
        return ""

# ============================================
# CHARACTER DEFINITIONS
# ============================================

define nicks_says = Character("Nicks", who_color='#ffaa00ff', image="nicks")
define aftb_says = Character("Aftb", who_color='#00aaffff', image="aftb")
define shas_says = Character("Shas", who_color='#080d27ff', image="shas")
define aman_says = Character("Aman", who_color='#00ff00ff', image="aman")
define abhi_says = Character("Abhi", who_color='#ffff00ff', image="abhi")
define aryn_says = Character("Aryn", who_color='#380c0cff', image="aryn")
define kernel_says = Character("Kernel", who_color='#8800ffff', image="kernel")
define roman_says = Character("Roman", who_color='#0088ffff', image="roman")
define jund_says = Character("Jund", who_color='#ff8800ff', image="jund")

label dayone_hostel_intro:
    scene scene_305_madd_sleep
    with fade
    x "I slept like a baby last night. The bed was surprisingly comfortable."
    x "Now, time to explore my new home away from that shitty home."
    jump hostel_exploration

# ============================================
# MAIN EXPLORATION LOOP
# ============================================

label hostel_exploration:
    # Show the time display screen
    show screen game_time_display
    
    # Show current location description
    call show_location_description from _call_show_location_description
    
    # Show exploration menu
    call show_exploration_menu from _call_show_exploration_menu
    
    # Return to exploration loop
    jump hostel_exploration

# ============================================
# LOCATION DESCRIPTIONS
# ============================================

label show_location_description:
    if current_location == "room":
        call maddroom_show_description from _call_maddroom_show_description
    
    elif current_location == "madds_bathroom":
        call maddroom_bathroom_show_description from _call_maddroom_bathroom_show_description
    
    elif current_location == "hallway_3rd":
        call floor_3_show_description from _call_floor_3_show_description
    
    elif current_location == "floor_1":
        call floor_1_show_description from _call_floor_1_show_description
    
    elif current_location == "floor_2":
        call floor_2_show_description from _call_floor_2_show_description
    
    elif current_location == "floor_4":
        call floor_4_show_description from _call_floor_4_show_description
    
    elif current_location == "reception":
        call reception_show_description from _call_reception_show_description
    
    elif current_location == "tv_room":
        call tv_room_show_description from _call_tv_room_show_description
    
    elif "_room" in current_location and "_bathroom" in current_location:
        # Character bathroom locations
        $ char_name = current_location.split("_room_bathroom")[0]
        $ renpy.call(char_name + "_room_bathroom_show_description")
    
    elif "_room" in current_location:
        # Character room locations
        $ char_name = current_location.split("_room")[0]
        $ renpy.call(char_name + "_room_show_description")
    
    return

# ============================================
# EXPLORATION MENU SYSTEM
# ============================================

label show_exploration_menu:
    # Menu for player's room
    if current_location == "room":
        call maddroom_show_menu from _call_maddroom_show_menu
    
    # Menu for bathroom
    elif current_location == "madds_bathroom":
        call maddroom_bathroom_show_menu from _call_maddroom_bathroom_show_menu
    
    # Menu for 3rd floor hallway
    elif current_location == "hallway_3rd":
        call floor_3_show_menu from _call_floor_3_show_menu
    
    # Menu for 1st Floor (Dining & Reception)
    elif current_location == "floor_1":
        call floor_1_show_menu from _call_floor_1_show_menu
    
    # Menu for 2nd Floor
    elif current_location == "floor_2":
        call floor_2_show_menu from _call_floor_2_show_menu
    
    # Menu for 4th Floor
    elif current_location == "floor_4":
        call floor_4_show_menu from _call_floor_4_show_menu
    
    # Menu for reception
    elif current_location == "reception":
        call reception_show_menu from _call_reception_show_menu
    
    # Menu for TV room
    elif current_location == "tv_room":
        call tv_room_show_menu from _call_tv_room_show_menu
    
    # Character bathrooms
    elif "_room_bathroom" in current_location:
        $ char_name = current_location.split("_room_bathroom")[0]
        $ renpy.call(char_name + "_room_bathroom_show_menu")
    
    # Character rooms
    elif "_room" in current_location:
        $ char_name = current_location.split("_room")[0]
        $ renpy.call(char_name + "_room_show_menu")
    
    return


# ============================================
# FLOOR EXPLORATION SUBMENUS
# ============================================

label explore_go_to_floor:
    x "Which floor would I like to go to?"
    
    menu:
        "Go to 1st Floor (Dining & Reception)":
            $ previous_location = current_location
            $ current_location = "floor_1"
            $ game_time.advance_time(minutes=3)
            call check_for_interception from _call_check_for_interception_3
        
        "Go to 2nd Floor":
            $ previous_location = current_location
            $ current_location = "floor_2"
            $ game_time.advance_time(minutes=2)
            call check_for_interception from _call_check_for_interception_4
        
        "Go to 3rd Floor (your room)":
            $ previous_location = current_location
            $ current_location = "hallway_3rd"
            $ game_time.advance_time(minutes=2)
            call check_for_interception from _call_check_for_interception_5
        
        "Go to 4th Floor":
            $ previous_location = current_location
            $ current_location = "floor_4"
            $ game_time.advance_time(minutes=2)
            call check_for_interception from _call_check_for_interception_6
        
        "Return to previous choice":
            pass
    
    return


# ============================================
# CHARACTER INTERACTIONS
# ============================================

# Character interaction labels have been moved to individual character files
# (nicks.rpy, roman.rpy, aftb.rpy, jund.rpy, shas.rpy, aman.rpy, abhi.rpy, aryn.rpy, mayank.rpy)
# Labels are now called from those files instead of being defined here
# Interception system is now in Charintercept.rpy

# ============================================
# TIME DISPLAY SCREEN
# ============================================

transform hud_time_fade:
    alpha 0.25
    on hover:
        linear 0.15 alpha 1.0
    on idle:
        linear 0.15 alpha 0.25

screen game_time_display():
    zorder 100
    if not _windows_hidden:
        # Date, Day, and Time display
        button at hud_time_fade:
            xpos 20
            ypos 20
            action NullAction()
            background None
            hover_background None
            text "📅 [game_time.get_date_string()] [get_day_of_week()] | ⏰ [game_time.get_time_string()]":
                size 24
                color "#ffffff"
                outlines [(1, "#000000", 0, 0)]





# ============================================
# TIME DISPLAY SCREEN
# ============================================
