

# ============================================
# CHARACTER INTERCEPTION SYSTEM - FUNCTIONS
# ============================================

init python:
    def get_characters_that_can_intercept(current_location, new_location, game_time, character_meal_times, character_water_times, character_door_open_times, met_characters, character_relations, travel_time_minutes):
        """
        Get list of characters that can intercept Madd when moving to a new location.
        Requirements:
        - Must have been met
        - Friendship > 10
        - Lust > 20
        - Must be at the current location OR destination location at arrival time
        - Probability is based on lust level
        Returns list of tuples: (character, intercept_probability)
        """
        interceptable = []
        
        # Calculate arrival time at new location
        arrival_hour = game_time.hour
        arrival_minute = game_time.minute + travel_time_minutes
        
        if arrival_minute >= 60:
            arrival_hour += arrival_minute // 60
            arrival_minute = arrival_minute % 60
        
        if arrival_hour >= 24:
            arrival_hour = arrival_hour % 24
        
        # Create a temporary game time object for the new location
        future_time = GameTime(arrival_hour, arrival_minute)
        
        characters_at_location = []
        
        # Check who is at current location or destination location
        for location in [current_location, new_location]:
            if location == "floor_2":
                # Check water cooler
                current_time_minutes = future_time.hour * 60 + future_time.minute
                for character, water_slots in character_water_times.items():
                    for slot_hour, slot_minute in water_slots:
                        slot_start_minutes = slot_hour * 60 + slot_minute
                        slot_end_minutes = slot_start_minutes + 15
                        if slot_start_minutes <= current_time_minutes < slot_end_minutes:
                            if character not in characters_at_location:
                                characters_at_location.append(character)
                
                # Check door open times
                for character, (door_hour, door_minute) in character_door_open_times.items():
                    slot_start_minutes = door_hour * 60 + door_minute
                    slot_end_minutes = slot_start_minutes + 30
                    if slot_start_minutes <= current_time_minutes < slot_end_minutes:
                        if character not in characters_at_location:
                            characters_at_location.append(character)
            
            elif location == "floor_1" or location == "messhall":
                # Check who is eating at mess hall
                current_time_minutes = future_time.hour * 60 + future_time.minute
                for character, meal_times in character_meal_times.items():
                    # Check which meal is happening
                    if 7 <= future_time.hour < 9:
                        meal_type = "breakfast"
                    elif 12 <= future_time.hour < 14:
                        meal_type = "lunch"
                    elif 19 <= future_time.hour < 21:
                        meal_type = "dinner"
                    else:
                        meal_type = None
                    
                    if meal_type and meal_type in meal_times:
                        slot_hour, slot_minute = meal_times[meal_type]
                        slot_start_minutes = slot_hour * 60 + slot_minute
                        slot_end_minutes = slot_start_minutes + 30
                        if slot_start_minutes <= current_time_minutes < slot_end_minutes:
                            if character not in characters_at_location:
                                characters_at_location.append(character)
        
        # Filter for valid interception candidates
        for character in characters_at_location:
            if character in met_characters and character in character_relations:
                rel = character_relations[character]
                if rel["friend"] > 10 and rel["lust"] > 50:
                    # Calculate interception probability based on lust (0-1 scale)
                    # Lust ranges from 0-100, so probability = lust / 100
                    base_probability = rel["lust"] / 100.0
                    interceptable.append((character, base_probability))  # Divided by 3 to reduce frequency
        
        return interceptable
    
    def can_madd_ignore(character, madd_dominance, character_relations):
        """
        Check if Madd can ignore a character based on dominance difference.
        If difference > 25, Madd cannot ignore and must interact.
        Returns True if Madd can ignore, False if forced to interact.
        """
        character_dominance = character_relations[character]["dominance"]
        dominance_diff = character_dominance - madd_dominance
        
        # If character's dominance is higher than Madd's, Madd must interact
        if dominance_diff > 0:
            return False
        return True

# ============================================
# CHARACTER INTERCEPTION SYSTEM - LABELS
# ============================================

label check_for_interception:
    # Interception check with character details
    python:
        global interceptions_today, last_interception_hour
        # Reset interceptions if it's a new day
        if game_time.hour < last_interception_hour and last_interception_hour != -1:
            interceptions_today = 0

    # Check if we've already had 3 interceptions today
    if interceptions_today >= 3:
        return

    python:
        # Get all characters present in area (regardless of interception eligibility)
        from_location = current_location
        arrival_hour = game_time.hour
        arrival_minute = game_time.minute + 2
        if arrival_minute >= 60:
            arrival_hour += arrival_minute // 60
            arrival_minute = arrival_minute % 60
        if arrival_hour >= 24:
            arrival_hour = arrival_hour % 24
        
        future_time = GameTime(arrival_hour, arrival_minute)
        
        characters_in_area = set()
        
        # Check all locations for characters
        for location in [from_location, current_location]:
            if location == "floor_2":
                current_time_minutes = future_time.hour * 60 + future_time.minute
                for character, water_slots in character_water_times.items():
                    for slot_hour, slot_minute in water_slots:
                        slot_start_minutes = slot_hour * 60 + slot_minute
                        slot_end_minutes = slot_start_minutes + 15
                        if slot_start_minutes <= current_time_minutes < slot_end_minutes:
                            characters_in_area.add(character)
                for character, (door_hour, door_minute) in character_door_open_times.items():
                    slot_start_minutes = door_hour * 60 + door_minute
                    slot_end_minutes = slot_start_minutes + 30
                    if slot_start_minutes <= current_time_minutes < slot_end_minutes:
                        characters_in_area.add(character)
            elif location == "floor_1" or location == "messhall":
                current_time_minutes = future_time.hour * 60 + future_time.minute
                for character, meal_times in character_meal_times.items():
                    if 7 <= future_time.hour < 9:
                        meal_type = "breakfast"
                    elif 12 <= future_time.hour < 14:
                        meal_type = "lunch"
                    elif 19 <= future_time.hour < 21:
                        meal_type = "dinner"
                    else:
                        meal_type = None
                    if meal_type and meal_type in meal_times:
                        slot_hour, slot_minute = meal_times[meal_type]
                        slot_start_minutes = slot_hour * 60 + slot_minute
                        slot_end_minutes = slot_start_minutes + 30
                        if slot_start_minutes <= current_time_minutes < slot_end_minutes:
                            characters_in_area.add(character)
        
        # Store character info for display
        characters_to_display = []
        for char in sorted(characters_in_area):
            if char in character_relations:
                rel = character_relations[char]
                char_info = "[char.capitalize()]: Friend=[rel['friend']], Lust=[rel['lust']], Identity=[rel['identity']], Dominance=[rel['dominance']], Anger=[rel['anger']]"
                characters_to_display.append((char, char_info, rel))
        
        all_names = ", ".join(sorted(characters_in_area)) if characters_in_area else "No one"
        
        # Now get characters that can actually intercept
        interceptable = get_characters_that_can_intercept(
            from_location,
            current_location, 
            game_time, 
            character_meal_times, 
            character_water_times, 
            character_door_open_times, 
            met_characters, 
            character_relations,
            2  # Default travel time of 2 minutes
        )

    # Display character information
    if characters_in_area:
        python:
            display_text = "I notice " + all_names + " in the area.\n"
            for char, char_info, rel in characters_to_display:
                display_text += char_info + "\n"
            renpy.say(x, display_text.strip())

    if interceptable:
        python:
            # Calculate who actually intercepts based on lust probability
            interceptor = None
            for character, probability in interceptable:
                if renpy.random.random() < probability:
                    interceptor = character
                    break
        
        if interceptor:
            # Interception happens silently
            $ interceptions_today += 1
            $ last_interception_hour = game_time.hour
            call intercept_scene(interceptor) from _call_intercept_scene
    
    return

label intercept_scene(interceptor):
    """
    Scene where a character catches Madd while trying to leave.
    Increases their lust, identity, dominance.
    Decreases Madd's dominance.
    """
    show madd boy cool at left_small
    with dissolve
    x "I'm trying to hurry along when I feel a hand on my shoulder."
    
    if interceptor == "nicks":
        call intercept_nicks from _call_intercept_nicks
    elif interceptor == "roman":
        call intercept_roman from _call_intercept_roman
    elif interceptor == "aftb":
        call intercept_aftb from _call_intercept_aftb
    elif interceptor == "shas":
        call intercept_shas from _call_intercept_shas
    elif interceptor == "aman":
        call intercept_aman from _call_intercept_aman
    elif interceptor == "jund":
        # Jund doesn't have strong dominance, so he might not intercept
        show jund at right_small
        with dissolve
        jund_says "Hey, [mainname]! Where are you headed?"
        show madd boy try to dodge at left_small
        with dissolve
        x "Oh, just around. How are you?"
        show jund at right_small
        with dissolve
        jund_says "Doing good! See you around!"
    elif interceptor == "abhi":
        # Abhi is friendly, so gentle interaction
        show abhi smile at right_small
        with dissolve
        abhi_says "Hey neighbor! Where you off to?"
        show madd boy happy at left_small
        with dissolve
        x "Just heading out. You?"
        show abhi laugh at right_small
        with dissolve
        abhi_says "Same here! See you!"
    elif interceptor == "aryn":
        # Aryn is friendly, so gentle interaction
        show aryn at right_small
        with dissolve
        aryn_says "Oh, [mainname]! How are you?"
        show madd boy happy at left_small
        with dissolve
        x "Doing well! You?"
        show aryn at right_small
        with dissolve
        aryn_says "Great! Talk later?"
    
    # Update character stats for those who intercept meaningfully
    if interceptor in ["nicks", "roman", "aftb", "shas", "aman"]:
        $ character_relations[interceptor]["lust"] += 4
        $ character_relations[interceptor]["identity"] += 3
        $ character_relations[interceptor]["dominance"] += 2
        $ madd_dominance -= 3
        $ madd_secret_identity = max(madd_secret_identity - 1, 0)
    
    $ game_time.advance_time(minutes=5)
    return

