



















# ============================================
# MESS HALL EATING SYSTEM
# ============================================

label eat_at_mess_hall:
    # Check for interception when entering mess hall
    $ old_location = current_location
    $ current_location = "messhall"
    call check_for_interception from _call_check_for_interception_9
    
    $ meal = game_time.get_meal_available()
    
    # Determine which scene and characters to show based on meal type
    if meal == "breakfast":
        scene scene_messhall_breakfast
        with fade
        $ eating_characters = get_characters_at_messhall(game_time, character_meal_times, "breakfast")
        show madd boy think at left_small
        with dissolve
        x "I enter the mess hall for breakfast."
    elif meal == "lunch":
        scene scene_messhall_breakfast
        with fade
        $ eating_characters = get_characters_at_messhall(game_time, character_meal_times, "lunch")
        show madd boy think at left_small
        with dissolve
        x "I enter the mess hall for lunch."
    elif meal == "dinner":
        scene scene_messhall_dinner
        with fade
        $ eating_characters = get_characters_at_messhall(game_time, character_meal_times, "dinner")
        show madd boy think at left_small
        with dissolve
        x "I enter the mess hall for dinner."
    else:
        scene scene_1f_morning
        with fade
        $ eating_characters = []
        show madd boy think at left_small
        with dissolve
        x "The dining area is not serving meals right now, but I can still hang out here."
    
    # Show available food options and character interactions
    python:
        eating_unmet = [char for char in eating_characters if char not in met_characters]
        eating_met = [char for char in eating_characters if char in met_characters]
    
    menu:
        "Grab fast food" if meal:
            show madd boy happy at left_small
            with dissolve
            x "I grab some fast food and find a spot to eat."
            if eating_characters:
                x "As I eat, I notice some people around the mess hall."
                if eating_unmet:
                    x "There are some new faces I haven't met yet."
                if eating_met:
                    x "I see some familiar faces."
            else:
                x "The mess hall is pretty quiet right now."
            $ game_time.advance_time(minutes=20)
            $ current_location = "floor_1"
            return
        
        "Grab a coke":
            show madd boy think at left_small
            with dissolve
            x "I grab a cold coke to drink."
            if eating_characters:
                x "I look around the mess hall."
                if eating_unmet:
                    x "There are some people here I haven't met yet."
                if eating_met:
                    x "I see some familiar faces."
            else:
                x "I find a seat and enjoy my drink."
            $ game_time.advance_time(minutes=10)
            $ current_location = "floor_1"
            return
        
        "Interact with someone" if eating_characters:
            call eat_and_interact(eating_characters, eating_unmet, eating_met, meal) from _call_eat_and_interact
            $ current_location = "floor_1"
            return
        
        "Return to 1st Floor":
            show madd boy think at left_small
            with dissolve
            x "I decide to leave the mess hall and head back."
            $ current_location = "floor_1"
            call check_for_interception from _call_check_for_interception_10
            $ game_time.advance_time(minutes=2)
            return
        
        "Wait here" if not meal:
            x "I decide to wait here for a bit."
            menu:
                "Wait 5 minutes":
                    $ game_time.advance_time(minutes=5)
                    call check_mayank_visit from _call_check_mayank_visit
                    # Only do interception check if Mayank didn't visit
                    if not mayank_visited_today:
                        call check_for_interception from _call_check_for_interception_11
                "Wait 15 minutes":
                    $ game_time.advance_time(minutes=15)
                    call check_mayank_visit from _call_check_mayank_visit_1
                    # Only do interception check if Mayank didn't visit
                    if not mayank_visited_today:
                        call check_for_interception from _call_check_for_interception_12
                "Wait 30 minutes":
                    $ game_time.advance_time(minutes=30)
                    call check_mayank_visit from _call_check_mayank_visit_2
                    # Only do interception check if Mayank didn't visit
                    if not mayank_visited_today:
                        call check_for_interception from _call_check_for_interception_13
                "Never mind":
                    pass
            $ current_location = "floor_1"
            return
        
        "Just pass through":
            show madd boy rbf at left_small
            with dissolve
            x "I decide not to stay long."
            $ game_time.advance_time(minutes=2)
            $ current_location = "floor_1"
            return
    
    return

label eat_and_interact(eating_characters, eating_unmet, eating_met, meal):
    # Show options to interact with characters - both unmet and met
    x "I see some people here. Should I approach someone?"
    
    menu:
        "Talk to Nicks" if "nicks" in eating_unmet:
            call interact_nicks_mess_hall(meal) from _call_interact_nicks_mess_hall
            return
        
        "Chat with Nicks" if "nicks" in eating_met:
            call interact_nicks_mess_hall_met(meal) from _call_interact_nicks_mess_hall_met
            return
        
        "Talk to Roman" if "roman" in eating_unmet:
            call interact_roman_mess_hall(meal) from _call_interact_roman_mess_hall
            return
        
        "Chat with Roman" if "roman" in eating_met:
            call interact_roman_mess_hall_met(meal) from _call_interact_roman_mess_hall_met
            return
        
        "Talk to Aftb" if "aftb" in eating_unmet:
            call interact_aftb_mess_hall(meal) from _call_interact_aftb_mess_hall
            return
        
        "Chat with Aftb" if "aftb" in eating_met:
            call interact_aftb_mess_hall_met(meal) from _call_interact_aftb_mess_hall_met
            return
        
        "Talk to Jund" if "jund" in eating_unmet:
            call interact_jund_mess_hall(meal) from _call_interact_jund_mess_hall
            return
        
        "Chat with Jund" if "jund" in eating_met:
            call interact_jund_mess_hall_met(meal) from _call_interact_jund_mess_hall_met
            return
        
        "Talk to Shas" if "shas" in eating_unmet:
            call interact_shas_mess_hall(meal) from _call_interact_shas_mess_hall
            return
        
        "Chat with Shas" if "shas" in eating_met:
            call interact_shas_mess_hall_met(meal) from _call_interact_shas_mess_hall_met
            return
        
        "Talk to Aman" if "aman" in eating_unmet:
            call interact_aman_mess_hall(meal) from _call_interact_aman_mess_hall
            return
        
        "Chat with Aman" if "aman" in eating_met:
            call interact_aman_mess_hall_met(meal) from _call_interact_aman_mess_hall_met
            return
        
        "Talk to Abhi" if "abhi" in eating_unmet:
            call interact_abhi_mess_hall(meal) from _call_interact_abhi_mess_hall
            return
        
        "Chat with Abhi" if "abhi" in eating_met:
            call interact_abhi_mess_hall_met(meal) from _call_interact_abhi_mess_hall_met
            return
        
        "Talk to Aryn" if "aryn" in eating_unmet:
            call interact_aryn_mess_hall(meal) from _call_interact_aryn_mess_hall
            return
        
        "Chat with Aryn" if "aryn" in eating_met:
            call interact_aryn_mess_hall_met(meal) from _call_interact_aryn_mess_hall_met
            return
        
        "Never mind":
            show madd boy think at left_small
            with dissolve
            x "I decide to just eat quietly."
            $ game_time.advance_time(minutes=15)
            return
    
    return
# MESS HALL CHARACTER INTERACTIONS
# ============================================
# Unmet character interactions are in individual character files
# Met character interactions (interact_CHAR_mess_hall_met) are also in individual files
# They are called from eat_and_interact
# They are called from eat_and_interact


